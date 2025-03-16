import asyncio
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
import json

# Load environment variables
load_dotenv()

# Initialize Tavily API key
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# Initialize FastMCP
mcp = FastMCP("web_search_tool")

# Initialize Tavily search tool
search_tool = TavilySearchResults(
    max_results=2,
    search_depth="basic",
    include_answer=True,
    include_raw_content=True,
    include_images=False
)

@mcp.tool()
async def search_web(query: str):
    """
    Search the web using Tavily API.
    
    Args:
        query (str): The search query string
        
    Returns:
        str: JSON formatted search results
    """
    try:
        # Execute the search
        response = await search_tool.ainvoke({"query": query})
        # response = "Search results will be displayed here"
        
        # Format the response
        formatted_response = {
            "status": "success",
            "results": response,
            "timestamp": asyncio.get_running_loop().time()
        }
        
        return json.dumps(formatted_response, indent=4)
    except Exception as e:
        error_response = {
            "status": "error",
            "message": str(e),
            "timestamp": asyncio.get_running_loop().time()
        }
        return json.dumps(error_response, indent=4)

if __name__ == "__main__":
    mcp.run(transport="stdio")