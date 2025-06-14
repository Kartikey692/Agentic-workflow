## LIVE LINK OF THE PROJECT - https://agentic-workflow-ia5o.onrender.com


🤖 Agentic Workflow with LangGraph & Mistral
This project demonstrates a robust agentic workflow using LangGraph and Mistral AI. The system can break down complex queries, execute tasks using integrated tools, reflect on results, and iteratively refine its approach to provide comprehensive answers—all accessible through a user-friendly Streamlit web interface.

📂 Project Structure
text
agentic-workflow/
├── app.py              # Streamlit web interface
├── tools.py            # Defines the web search and calculator tools
├── workflow.py         # Core LangGraph workflow logic (planning, execution, reflection)
├── requirements.txt    # Python dependencies
├── .env                # (Optional) Your API keys and environment variables
├── venv/               # Python virtual environment (optional, not included in repo)


🛠️ Tools Used
1. Web Search Tool (web_search)
Purpose: Fetches real-time information from the web.

How it works: Uses the DuckDuckGo Instant Answer API via the requests library. It returns concise summaries or related topics for general knowledge and factual queries.

2. Calculator Tool (calculator)
Purpose: Evaluates mathematical expressions.

How it works: Safely computes expressions using Python's eval() in a sandboxed environment, supporting standard math functions.

🚀 Quick Start
Clone the repository and navigate to the project folder:

bash
git clone <your-repository-url>
cd agentic-workflow
Create and activate a virtual environment (recommended):

On macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate
On Windows:

bash
python -m venv venv
.\venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Set your API key (if required, e.g., for Mistral):

Create a .env file in the project root and add:

text
MISTRAL_API_KEY="your_mistral_api_key_here"
(You may skip this if not using a key-protected model.)

Run the app:

bash
streamlit run app.py
The app will open in your browser at http://localhost:8501.

🧪 Example Queries
What is the distance between the Sun and Earth?

What is the population of India?

Calculate the result of (15 * 24) / 4.

Find the population of Canada and its largest city, then calculate what percentage of the country's population lives in that city.
