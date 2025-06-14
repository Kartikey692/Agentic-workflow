# #workflow.py
# import os
# from dotenv import load_dotenv
# from typing import TypedDict, Annotated, List
# from langchain_core.messages import BaseMessage, HumanMessage
# from langchain_mistralai import ChatMistralAI
# from langgraph.graph import StateGraph, END
# from langgraph.prebuilt import ToolNode
# from tools import get_tools

# # --- Load Environment Variables ---
# load_dotenv()

# # --- State Definition ---
# class AgentState(TypedDict):
#     messages: Annotated[List[BaseMessage], lambda x, y: x + y]

# # --- Workflow Nodes ---
# class AgenticWorkflow:
#     def __init__(self):
#         self.llm = ChatMistralAI(model="mistral-small-latest", temperature=0)
#         self.tools = get_tools()
#         self.llm_with_tools = self.llm.bind_tools(self.tools)
#         self.tool_node = ToolNode(self.tools)

#     def planner_node(self, state: AgentState):
#         """Uses the LLM to plan or continue reasoning based on tool output."""
#         response = self.llm_with_tools.invoke(state["messages"])
#         return {"messages": [response]}

#     def reflect_node(self, state: AgentState):
#         """Checks the last tool output to decide whether to retry or proceed."""
#         last_message = state["messages"][-1]
#         content = getattr(last_message, "content", "").lower()

#         # Detect failure cases (basic error heuristics)
#         if "error" in content or "not found" in content or "failed" in content:
#             retry_msg = "The previous result wasn't good. Try refining or rephrasing the task."
#             print("[Reflection] Triggering retry...")
#             state["messages"].append(HumanMessage(content=retry_msg))
#             return state, "retry"
#         else:
#             print("[Reflection] Output looks good, continuing...")
#             return state, "continue"

#     def router(self, state: AgentState):
#         """Decide whether to call a tool or return final answer."""
#         last_message = state["messages"][-1]
#         if hasattr(last_message, "tool_calls") and last_message.tool_calls:
#             return "call_tool"
#         return "END"

# # --- Build LangGraph ---
# def create_agentic_workflow():
#     workflow = StateGraph(AgentState)
#     agent = AgenticWorkflow()

#     # Nodes
#     workflow.add_node("agent", agent.planner_node)
#     workflow.add_node("call_tool", agent.tool_node)
#     workflow.add_node("reflect", agent.reflect_node)

#     # Entry
#     workflow.set_entry_point("agent")

#     # Planner decides whether to call a tool or end
#     workflow.add_conditional_edges(
#         "agent",
#         agent.router,
#         {
#             "call_tool": "call_tool",
#             "END": END,
#         },
#     )

#     # After calling the tool → reflect
#     workflow.add_edge("call_tool", "reflect")

#     # Reflection decides whether to retry or continue
#     workflow.add_conditional_edges(
#         "reflect",
#         lambda state: state[1],  # returns "retry" or "continue"
#         {
#             "retry": "agent",
#             "continue": "agent",
#         }
#     )

#     return workflow.compile()


# # workflow.py
# import os
# from dotenv import load_dotenv
# from typing import TypedDict, Annotated, List
# from langchain_core.messages import BaseMessage, HumanMessage
# from langchain_mistralai import ChatMistralAI
# from langgraph.graph import StateGraph, END
# from langgraph.prebuilt import ToolNode
# from tools import get_tools

# # --- Load Environment Variables ---
# load_dotenv()

# # --- Define Agent State ---
# class AgentState(TypedDict):
#     messages: Annotated[List[BaseMessage], lambda x, y: x + y]
#     tasks: List[str]
#     current_task: str

# # --- Define Workflow Class ---
# class AgenticWorkflow:
#     def __init__(self):
#         self.llm = ChatMistralAI(model="mistral-small-latest", temperature=0)
#         self.tools = get_tools()
#         self.llm_with_tools = self.llm.bind_tools(self.tools)
#         self.tool_node = ToolNode(self.tools)

#     def next_task_planner_node(self, state: AgentState) -> AgentState:
#         """Pick the next task from the list and add to message history."""
#         if not state["tasks"]:
#             return state  # No more tasks
#         task = state["tasks"].pop(0)
#         state["current_task"] = task
#         state["messages"].append(HumanMessage(content=task))
#         return state

#     def planner_node(self, state: AgentState) -> AgentState:
#         """LLM processes the message and possibly calls tools."""
#         response = self.llm_with_tools.invoke(state["messages"])
#         state["messages"].append(response)
#         return state

#     def reflect_node(self, state: AgentState) -> str:
#         """Decide whether the tool output was good or needs a retry."""
#         last_message = state["messages"][-1]
#         content = getattr(last_message, "content", "").lower()

#         if "error" in content or "not found" in content or "failed" in content:
#             return "retry"
#         return "continue"

#     def task_refiner_node(self, state: AgentState) -> AgentState:
#         """Modify, delete, or add tasks based on last result."""
#         last_output = state["messages"][-1].content.lower()
#         task = state["current_task"]

#         if "error" in last_output or "not found" in last_output:
#             # MODIFY task → retry with clarification
#             refined = f"Retry with clarification: {task}"
#             state["tasks"].append(refined)

#         elif "irrelevant" in last_output or "not needed" in last_output:
#             # DELETE task → just don't re-add

#             pass

#         elif "also check" in last_output or "consider looking" in last_output:
#             # ADD task → based on LLM suggestion
#             new_task = "Follow-up search based on results"
#             state["tasks"].append(new_task)

#         return state

#     def router(self, state: AgentState) -> str:
#         """Route to tool or end."""
#         last_message = state["messages"][-1]
#         if hasattr(last_message, "tool_calls") and last_message.tool_calls:
#             return "call_tool"
#         return "END"

# # --- Build the Graph ---
# def create_agentic_workflow():
#     workflow = StateGraph(AgentState)
#     agent = AgenticWorkflow()

#     # Add all nodes
#     workflow.add_node("next_task", agent.next_task_planner_node)
#     workflow.add_node("agent", agent.planner_node)
#     workflow.add_node("call_tool", agent.tool_node)
#     workflow.add_node("reflect", agent.reflect_node)
#     workflow.add_node("refine", agent.task_refiner_node)

#     # Define edges
#     workflow.set_entry_point("next_task")
#     workflow.add_edge("next_task", "agent")
#     workflow.add_conditional_edges("agent", agent.router, {
#         "call_tool": "call_tool",
#         "END": END
#     })
#     workflow.add_edge("call_tool", "reflect")
#     workflow.add_conditional_edges("reflect", lambda state: state, {
#         "retry": "refine",
#         "continue": "refine"
#     })
#     workflow.add_edge("refine", "next_task")

#     return workflow.compile()


# workflow.py
# workflow.py
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_mistralai import ChatMistralAI
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from tools import get_tools

# --- Load API keys from .env
load_dotenv()

# --- LangGraph State Schema
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]
    tasks: List[str]
    current_task: str

# --- Agent Workflow Class
class AgenticWorkflow:
    def __init__(self):
        self.llm = ChatMistralAI(model="mistral-small-latest", temperature=0)
        self.tools = get_tools()
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        self.tool_node = ToolNode(self.tools)

    # Step 1: Pick the next task
    def next_task_planner_node(self, state: AgentState) -> AgentState:
        if not state.get("tasks"):
            return state
        task = state["tasks"].pop(0)
        state["current_task"] = task
        state["messages"].append(HumanMessage(content=task))
        return state

    # Step 2: LLM handles the task (could call a tool)
    def planner_node(self, state: AgentState) -> AgentState:
        response = self.llm_with_tools.invoke(state["messages"])
        state["messages"].append(response)
        return state

    # Step 3: Decide based on tool output
    def reflect_node(self, state: AgentState) -> str:
        last_message = state["messages"][-1]
        content = getattr(last_message, "content", "").lower()

        if "error" in content or "not found" in content or "failed" in content:
            return "retry"
        return "continue"

    # Step 4: Refine the plan (modify/delete/add)
    def task_refiner_node(self, state: AgentState) -> AgentState:
        last_output = state["messages"][-1].content.lower()
        task = state["current_task"]

        if "error" in last_output or "not found" in last_output:
            refined = f"Retry with clarification: {task}"
            print(f"[Modify] Retrying with: {refined}")
            state["tasks"].append(refined)

        elif "irrelevant" in last_output or "not needed" in last_output:
            print(f"[Delete] Skipping task: {task}")

        elif "also check" in last_output or "consider looking" in last_output:
            followup = "Follow-up task based on previous output"
            print(f"[Add] New task added: {followup}")
            state["tasks"].append(followup)

        return state

    # Step 5: Decide next move
    def router(self, state: AgentState) -> str:
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "call_tool"
        return "END"

# --- Graph Builder
def create_agentic_workflow():
    workflow = StateGraph(AgentState)
    agent = AgenticWorkflow()

    workflow.add_node("next_task", agent.next_task_planner_node)
    workflow.add_node("agent", agent.planner_node)
    workflow.add_node("call_tool", agent.tool_node)
    workflow.add_node("reflect", agent.reflect_node)
    workflow.add_node("refine", agent.task_refiner_node)

    workflow.set_entry_point("next_task")
    workflow.add_edge("next_task", "agent")

    workflow.add_conditional_edges("agent", agent.router, {
        "call_tool": "call_tool",
        "END": END
    })

    workflow.add_edge("call_tool", "reflect")

    workflow.add_conditional_edges("reflect", agent.reflect_node, {
        "retry": "refine",
        "continue": "refine"
    })

    workflow.add_edge("refine", "next_task")

    return workflow.compile()
