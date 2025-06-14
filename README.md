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

├── app.py

├── tools.py

├── workflow.py

├── requirements.txt 

├── .env 

└── venv/ 


---

## 🛠️ Tools Used

### 1. Web Search Tool (`web_search`)
- **Purpose**: Fetches real-time data from the web.
- **How it works**: Uses the DuckDuckGo Instant Answer API with `requests` to return quick facts or summaries.

### 2. Calculator Tool (`calculator`)
- **Purpose**: Evaluates mathematical expressions.
- **How it works**: Safely computes expressions using Python’s `eval()` in a sandboxed environment. Supports common math functions.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd agentic-workflow


