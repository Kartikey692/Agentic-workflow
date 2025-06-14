import streamlit as st
from langchain_core.messages import HumanMessage
from workflow import create_agentic_workflow

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Agentic Workflow Demo", layout="wide")
st.title("🤖 Agentic Workflow with LangGraph & Mistral")
st.markdown(
    """
This app demonstrates a reliable agentic workflow. The agent can:
1.  **Plan**: Break down your request into steps.
2.  **Use Tools**: Use a web search tool and a calculator.
3.  **Reflect & Refine**: Analyze tool results and adjust its plan to reach the final answer.
"""
)

# --- Initialize Workflow ---
if "graph" not in st.session_state:
    st.session_state.graph = create_agentic_workflow()

# --- Chat History Management ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input and Workflow Execution ---
if prompt := st.chat_input("What would you like to do?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    inputs = {"messages": [HumanMessage(content=prompt)]}

    with st.spinner("Agent is thinking..."):
        events = st.session_state.graph.stream(inputs, stream_mode="values")
        
        final_response_message = None
        for value in events:
            last_message = value["messages"][-1]
            
            # --- THIS IS THE CORRECTED LOGIC ---
            # First, check if the message has tool_calls. HumanMessage won't.
            if hasattr(last_message, "tool_calls") and last_message.tool_calls:
                # This is an AIMessage with tool calls, so the agent is still working.
                # We can optionally display this to the user for clarity.
                # For example: st.write(f"Agent is calling tools: {last_message.tool_calls}")
                pass
            else:
                # This is either a HumanMessage or the final AIMessage without tool calls.
                # We save it as the potential final response.
                final_response_message = last_message

    # Display the final response from the agent
    if final_response_message:
        with st.chat_message("assistant"):
            st.markdown(final_response_message.content)
        st.session_state.messages.append({"role": "assistant", "content": final_response_message.content})

