# Web_Search_MCP
An MCP(Model Context Protocol) Server with a web search tool


This project demonstrates how to create a web search tool using the Tavily API and integrate it with FastMCP (Model Context Protocol) for seamless interaction with AI agents or other applications. This allows you to provide real-time web search capabilities to your language models or applications.

## Overview

The `Web_Search_MCP` project leverages the following key components:

*   **Tavily API:** A powerful search API that provides real-time, comprehensive web search results, including answers, raw content, and relevant metadata.
*   **FastMCP:** A Python library enabling the creation of tool servers based on the Model Context Protocol (MCP). This allows for easy integration of custom tools with AI models.
*   **Langchain:**  Specifically, the `TavilySearchResults` tool from Langchain is used to interact with the Tavily API efficiently.
*   **Dotenv:** A library for loading environment variables from a `.env` file, securely managing sensitive information like API keys.
*   **uvloop:** provides an implementation of asyncio that provides a high-performance event loop.
* **uv:** A very fast Python package installer and resolver, used to manage and run this project.

## Functionality

The core of this project lies within the `search_web` tool, which provides the following features:

*   **Web Search:** Accepts a search query as input and retrieves relevant search results from the web using the Tavily API.
*   **Detailed Results:**  Provides detailed information from the search results, including the website's content, URL, a relevancy score, the content type, and a direct answer (if available).
*   **Formatted Output:**  Returns the search results in a well-structured JSON format. The output includes a status indicator (`success` or `error`), an array of results (if successful), and a timestamp.
*   **Error Handling:** Gracefully handles errors during the search process and returns an informative error message in JSON format.
* **Asynchronous processing**: The search tool is based on asynchronous, which can handle many requests at the same time.

## Prerequisites

Before running the project, ensure that you have:

*   **Python 3.8+:** Python 3.8 or a later version installed on your system.
*   **Tavily API Key:** A valid Tavily API key, obtainable by signing up on the Tavily website.
*   **uv:**  The uv package manager for Python. You can install it using:
    ```bash
    pip install uv
    ```

## Installation

1.  **Create Project Directory:** Create a directory for the project and navigate into it:
    ```bash
    mkdir Web_Search_MCP
    cd Web_Search_MCP
    ```
2.  **Create Project Files:** Create the files `main.py` and `.env` in the `Web_Search_MCP` directory.
3.  **Copy code:** copy the code in the `main.py` and `.env` into the files you just create.
4.  **Install Dependencies:** Use `uv` to install the required Python packages:
    ```bash
    uv pip install mcp python-dotenv langchain-community uvloop tavily-python
    ```

## Configuration

1.  **`.env` File:**
    *   Create a file named `.env` in the `Web_Search_MCP` directory.
    *   Add your Tavily API key to the `.env` file in the following format:
        ```properties
        TAVILY_API_KEY='your_tavily_api_key'
        ```
        Replace `your_tavily_api_key` with your actual Tavily API key.

2.  **`claude_desktop_config.json`:**
    *   This file is used by the Claude desktop application (if you are using it) to discover and run the FastMCP server.
    *   It should reside in `c:\Users\<Your User Name>\AppData\Roaming\Claude\claude_desktop_config.json`
    * Ensure the path to your `Web_Search_MCP` directory in  `claude_desktop_config.json` is accurate. If your project is not in path/Web_Search_MCP` , please modify the `args` field in the config file.
     ```json
     {
        "mcpServers": {
          "Mcp_Demo": {
            "command": "uv",
            "args": [
              "--directory",
              "path/Web_Search_MCP",
              "run",
              "main.py"
            ]
          }
        }
      }
    ```

## Running the FastMCP Server

1.  **Navigate to the Project Directory:**
    ```bash
    cd path/Web_Search_MCP
    ```
    

2.  **Start the Server:** Run the following command using `uv`:
    ```bash
    uv run main.py
    ```
    Alternatively, if you have configured the `claude_desktop_config.json` file, you can start the server from within the Claude desktop application.

## Usage

Once the server is running, it exposes a single tool called `search_web` according to the Model Context Protocol.

*   **Tool Name:** `search_web`
*   **Input:**
    *   `query` (str): The search query you want to submit to the web.
*   **Output:**  A JSON formatted string containing the search results.

**Example JSON Response (Success):**

```json
{
    "status": "success",
    "results": [
        {
            "title": "...",
            "url": "...",
            "content": "text",
            "score": 0.9,
            "raw_content": "..."
        },
        {
             "title": "...",
            "url": "...",
            "content": "text",
            "score": 0.9,
            "raw_content": "..."
        }
    ],
    "timestamp": 1708849844.064655
}

