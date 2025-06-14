import requests
import math
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

# --- Web Search Tool ---
class SearchInput(BaseModel):
    query: str = Field(description="The search query to find information on the web.")

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "A tool to search the internet for information. Use this for up-to-date information or general knowledge questions."
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        """Execute web search using DuckDuckGo API."""
        try:
            url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get('AbstractText'):
                return f"Search Result for '{query}': {data['AbstractText']}"
            elif data.get('RelatedTopics'):
                topics = [t['Text'] for t in data['RelatedTopics'] if 'Text' in t]
                return f"Found related topics for '{query}': {', '.join(topics[:5])}"
            else:
                return f"No direct results found for '{query}'. Try a different search term."
        except Exception as e:
            return f"Error during search: {e}"

# --- Calculator Tool ---
class CalculatorInput(BaseModel):
    expression: str = Field(description="A valid mathematical expression to evaluate.")

class CalculatorTool(BaseTool):
    name: str = "calculator"
    description: str = "A tool to evaluate mathematical expressions. Use this for calculations."
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, expression: str) -> str:
        """Safely evaluate mathematical expressions."""
        try:
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return f"The result of '{expression}' is {result}"
        except Exception as e:
            return f"Error during calculation: {e}"

# Function to get all available tools
def get_tools():
    """Returns a list of all available tool instances."""
    return [WebSearchTool(), CalculatorTool()]


