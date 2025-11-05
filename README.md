# MCP FileFetch

A lightweight **FastAPI-based MCP server** that performs keyword-based searches inside a text file and returns the results as structured JSON.  
Built as part of the Ressl AI assessment to demonstrate backend API development and modular server design.

## Project Overview

The goal of this project is to:
- Build an MCP server using **FastAPI** and **Uvicorn**.
- Implement a tool that searches for a specified keyword in a text file.
- Return the search results in a clean JSON format.

## ⚙️ Tech Stack

- **Python 3.10+**
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server for running the FastAPI app

   ## Install dependencies
  - pip install -r requirements.txt
   ## Start the server
   - python app.py
  ## Test in your environment
  http://127.0.0.1:8000/search?keyword=AI
## Output 
<img width="1334" height="766" alt="image" src="https://github.com/user-attachments/assets/814e932b-43e2-43e7-9b5a-766e5c16da4d" />

## Future Enhancements 
- Upload the file dynamically
- Add semantic search using OpenAI embeddings or FAISS
- Integrate Salesforce API for live CRM data search
- Build a frontend UI or MCP Inspector for easier querying

  ## Author
  ### Yogita Adari
  Data Scientist | AI Engineer | Backend Developer
