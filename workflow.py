import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_mistralai import ChatMistralAI
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from tools import get_tools

# --- Load Environment Variables ---
load_dotenv()

# --- State Definition ---
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]

# --- Workflow Nodes ---
class AgenticWorkflow:
    def __init__(self):
        self.llm = ChatMistralAI(model="mistral-small-latest", temperature=0)
        self.tools = get_tools()
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        self.tool_node = ToolNode(self.tools)

    def planner_node(self, state: AgentState):
        """Uses the LLM to plan or continue reasoning based on tool output."""
        response = self.llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}

    # --- CHANGE 1: Fix the reflect_node ---
    # This node's only job is to update the state if a retry is needed.
    # It should NOT return a tuple.
    def reflect_node(self, state: AgentState):
        """Checks the last tool output to decide if a retry message should be added."""
        last_message = state["messages"][-1]
        content = getattr(last_message, "content", "").lower()

        # If the last tool call resulted in an error, add a message to the state
        # prompting the agent to retry.
        if "error" in content or "not found" in content or "failed" in content:
            print("[Reflection] Error detected, adding a retry message to the state.")
            retry_msg = HumanMessage(content="The previous tool call failed. Please analyze the error and try a different approach to solve the original request.")
            return {"messages": [retry_msg]}
        else:
            # If everything is fine, do not update the state.
            print("[Reflection] Output looks good, proceeding.")
            return {}

    # --- CHANGE 2: Create a NEW function for the conditional edge ---
    # This function's only job is to decide the next route.
    def should_retry(self, state: AgentState) -> str:
        """Determines whether to retry the agent or continue based on the last message."""
        last_message = state["messages"][-1]
        
        # If the reflect_node added a HumanMessage, it means we need to retry.
        if isinstance(last_message, HumanMessage):
            return "retry"
        
        # Otherwise, the last message is an AIMessage or ToolMessage, so we continue.
        # This logic is now simpler and more robust.
        return "continue"

    def router(self, state: AgentState):
        """Decide whether to call a tool or return final answer."""
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "call_tool"
        return "END"

# --- Build LangGraph ---
def create_agentic_workflow():
    workflow = StateGraph(AgentState)
    agent = AgenticWorkflow()

    # Nodes
    workflow.add_node("agent", agent.planner_node)
    workflow.add_node("call_tool", agent.tool_node)
    workflow.add_node("reflect", agent.reflect_node)

    # Entry
    workflow.set_entry_point("agent")

    # Planner decides whether to call a tool or end
    workflow.add_conditional_edges(
        "agent",
        agent.router,
        {
            "call_tool": "call_tool",
            "END": END,
        },
    )

    # After calling the tool → reflect
    workflow.add_edge("call_tool", "reflect")

    # --- CHANGE 3: Update the conditional edge to use the new function ---
    # Reflection decides whether to retry or continue to the planner.
    workflow.add_conditional_edges(
        "reflect",
        agent.should_retry,  # Use the new, dedicated routing function
        {
            "retry": "agent",
        
            "continue": "agent",
        }
    )

    return workflow.compile()
