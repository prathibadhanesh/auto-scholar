# AutoScholar Implementation Plan

AutoScholar is defined as a health research assistant where specialized agents are utilized to search for and summarize medical literature. Ollama (gemma3:1b) is leveraged for reasoning and Streamlit is used for the interface.

## Proposed Changes

### Project Structure
The project is structured as follows:
- app.py: Central Streamlit application.
- agents/searcher.py: Searcher agent implementation using the arXiv API.
- agents/summarizer.py: Summarizer agent implementation.
- database/vector_store.py: Vector search functionality using ChromaDB.
- README.md: Project overview and setup instructions.
- AGENTS.md: Documentation for agent roles and coordination logic.
- requirements.txt: Project dependencies.

---

### Components

#### [requirements.txt](file:///home/pdhanesh/code/auto-scholar/requirements.txt)
Dependencies are defined, including `streamlit`, `ollama`, `chromadb`, and `arxiv`.

#### [vector_store.py](file:///home/pdhanesh/code/auto-scholar/database/vector_store.py)
Document storage and retrieval are handled via a class using ChromaDB.

#### [searcher.py](file:///home/pdhanesh/code/auto-scholar/agents/searcher.py)
Relevant medical and health research papers are found and downloaded using the arXiv API.

#### [summarizer.py](file:///home/pdhanesh/code/auto-scholar/agents/summarizer.py)
Findings are summarized using gemma3:1b via Ollama.

#### [app.py](file:///home/pdhanesh/code/auto-scholar/app.py)
Agent coordination and result display are managed by the UI.

#### [README.md](file:///home/pdhanesh/code/auto-scholar/README.md)
A project overview, installation guide, and usage instructions are provided.

#### [AGENTS.md](file:///home/pdhanesh/code/auto-scholar/AGENTS.md)
Agent roles, prompts, and coordination logic are documented.

---

## Verification Plan

### Automated Tests
- Search results are verified by executing `python -m agents.searcher`.
- The LLM connection is confirmed by executing `python -m agents.summarizer`.
- ChromaDB storage is validated by executing `python -m database.vector_store`.

### Manual Verification
- The Streamlit UI is launched via `streamlit run app.py`.
- A search for a specific medical topic (e.g., "benefits of Vitamin D") is performed.
- Results are inspected to ensure they are found, summarized, and correctly retrieved from the vector store.
