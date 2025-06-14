# 🤖 Agentic Workflow with LangGraph & Mistral

**Live Demo**: https://agentic-workflow-ia5o.onrender.com

This project demonstrates a robust **agentic workflow** using **LangGraph** and **Mistral AI**. The system is capable of:

- Decomposing complex user queries into manageable tasks
- Executing those tasks using integrated tools
- Reflecting on intermediate results
- Iteratively refining its answers for maximum accuracy

All of this is exposed through a user-friendly **Streamlit web interface**.

---

## 📁 Project Structure

agentic-workflow/
├── app.py # Streamlit web interface
├── tools.py # Web search and calculator tool definitions
├── workflow.py # Core LangGraph logic (planning, execution, reflection)
├── requirements.txt # Python dependencies
├── .env # (Optional) API keys and environment variables
└── venv/ # (Optional) Python virtual environment

