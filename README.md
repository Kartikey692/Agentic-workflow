## LIVE LINK OF THE PROJECT - https://agentic-workflow-ia5o.onrender.com


### Agentic Workflow with LangGraph & Mistral
This project demonstrates a reliable agentic workflow built with LangGraph and powered by Mistral AI. The system uses a planner-reflector model to handle complex user queries. It can break down requests into steps, execute tasks using tools, reflect on the results to handle errors, and provide a final answer through a clean Streamlit web interface.



### Agent Tools
The agent is equipped with the following tools to interact with its environment:

1. Web Search
Tool Name: web_search

Description: A tool for searching the internet for information. It is best used for up-to-date information or general knowledge questions.

How it Works: This tool sends a query to the DuckDuckGo Instant Answer API using the requests library. It parses the JSON response to extract the most relevant abstract text or related topics, returning a concise summary to the agent.

2. Calculator
Tool Name: calculator

Description: A tool designed to evaluate mathematical expressions and perform calculations.

How it Works: It safely evaluates a string containing a mathematical expression using Python's eval() function. The execution is sandboxed to only allow access to standard math functions for security.



### How to Run
To run this project, first clone the repository, then create and activate a Python virtual environment. Install all required packages by running pip install -r requirements.txt. Next, create a .env file in the project's root directory and add your MISTRAL_API_KEY="your_key_here". Finally, launch the interactive web application with the command streamlit run app.py, and it will open in your browser.


