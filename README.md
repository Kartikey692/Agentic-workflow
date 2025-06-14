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

## 🚀 How To Run 


1. Clone the Repository :

       git clone  <your-repository-url>

       cd agentic-workflow


2. Create Virtual Environment:

    On macOS/Linux:

       python3 -m venv venv

       source venv/bin/activate

    On Windows:

       python -m venv venv

       .\venv\Scripts\activate


3. Install Dependencies:
   
       pip install -r requirements.txt


4. Set Environment Variables 

       Create a .env file in the project root and add:

       MISTRAL_API_KEY="your_mistral_api_key_here"


5. Run the App
   
       streamlit run app.py

The app will open in your browser at http://localhost:8501.




🧪 Example Queries
What is the distance between the Sun and Earth?

What is the population of India?

Calculate the result of (15 * 24) / 4.

Find the Distance Between Earth and Moon, then find what is 35 percent of that Distance.




