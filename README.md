### LIVE LINK OF THE PROJECT - https://agentic-workflow-ia5o.onrender.com

🤖 Agentic Workflow with LangGraph & Mistral
This project demonstrates a reliable agentic workflow built with LangGraph and powered by Mistral AI.
The system uses a planner-reflector-executor model to handle complex user queries. It can:

Break down requests into sub-tasks
Execute those tasks using tools (like search & calculator)
Reflect on results to handle errors or refine queries
Provide a final answer through a Streamlit web interface

📂 Project Structure
The project is organized into a few key files for simplicity and clarity:

agentic-workflow/
├── venv/                # Optional: your Python virtual environment
├── .env                 # Stores API keys and environment variables
├── app.py               # The Streamlit web interface for user interaction
├── requirements.txt     # Lists all necessary Python packages
├── tools.py             # Defines tools the agent can use (e.g., search, calculator)
└── workflow.py          # Contains the core LangGraph agentic workflow logic

🛠️ Agent Tools
The agent uses the following tools to accomplish tasks:

🔍 Web Search Tool
Tool Name: web_search

Description: Searches the internet for information — ideal for real-time data or general knowledge.

How it Works: Sends a query to the Tavily Web Search API, then extracts and summarizes relevant results.

➗ Calculator Tool
Tool Name: calculator

Description: Evaluates mathematical expressions and performs calculations.

How it Works: Uses Python's built-in eval() inside a secure environment to calculate expressions like "8% of 1000" or "1000 * 0.08".      


🚀 How to Run
1.Clone the repository
2.Create and activate a virtual environment
3.Install required dependencies
4.Create a .env file and add your API key
5.Launch the Streamlit app


