# AutoScholar Implementation Plan

AutoScholar is a health research assistant that uses specialized agents to search for and summarize medical literature. It leverages Ollama (llama3) for reasoning and Streamlit for the interface.

## Proposed Changes

### Project Structure
[NEW] We will create the following structure:
- `app.py`: Main Streamlit application.
- `agents/searcher.py`: Searcher agent using arXiv API.
- `agents/summarizer.py`: Summarizer agent implementation.
- `database/vector_store.py`: Simple vector search using ChromaDB.
- `README.md`: Project overview and setup instructions.
- `AGENTS.md`: Detailed documentation for the searcher and summarizer agents.
- `requirements.txt`: Project dependencies.

---

### Components

#### [NEW] [requirements.txt](file:///home/pdhanesh/code/auto-scholar/requirements.txt)
Define dependencies: `streamlit`, `ollama`, `chromadb`, `arxiv`.

#### [NEW] [vector_store.py](file:///home/pdhanesh/code/auto-scholar/database/vector_store.py)
A class to handle document storage and retrieval using ChromaDB.

#### [NEW] [searcher.py](file:///home/pdhanesh/code/auto-scholar/agents/searcher.py)
An agent that uses the `arxiv` API to find and download relevant medical/health research papers.

#### [NEW] [summarizer.py](file:///home/pdhanesh/code/auto-scholar/agents/summarizer.py)
An agent that uses `llama3` via Ollama to summarize the findings.

#### [NEW] [app.py](file:///home/pdhanesh/code/auto-scholar/app.py)
The UI to coordinate the agents and display results.

#### [NEW] [README.md](file:///home/pdhanesh/code/auto-scholar/README.md)
Project overview, installation guide, and usage instructions.

#### [NEW] [AGENTS.md](file:///home/pdhanesh/code/auto-scholar/AGENTS.md)
Documentation of agent roles, prompts, and coordination logic.

---

## Verification Plan

### Automated Tests
- Run `python -m agents.searcher` (with a test main) to verify search results.
- Run `python -m agents.summarizer` (with a test main) to verify LLM connection.
- Run `python -m database.vector_store` to verify ChromaDB storage.

### Manual Verification
- Launch Streamlit UI: `streamlit run app.py`.
- Search for a specific medical topic (e.g., "benefits of Vitamin D").
- Verify that the searcher finds results, the summarizer summarizes them, and they are saved/retrieved from the vector store.
