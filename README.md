#  Agentic Workflow with LangGraph, Mistral, and Streamlit

This project demonstrates an **agentic AI workflow** using [LangGraph](https://github.com/langchain-ai/langgraph), where an agent can:
- Plan tasks from a complex query
- Use external tools (like web search and calculator)
- Reflect on tool outputs
- Refine, retry, or add new tasks automatically

Built with:
-  [Mistral AI](https://mistral.ai/) as the LLM
-  LangGraph for agent flow
-  Custom Tools: Web Search + Calculator
-  Streamlit UI for interaction

---

## Features

-  Query planning (breaks down user input into sub-tasks)
-  Tool invocation via function calling (web search & math)
-  Reflection + Feedback: retry/refine steps if needed
-  Modular code (tools, agent, workflow separated)
-  Streamlit interface for live testing

---


