# AutoScholar: Health Research Agent

AutoScholar is an AI-powered research assistant designed to search, re-rank, and summarize medical and health-related literature. It combines the arXiv API for broad discovery with a lightweight LLM (Gemma 3 1B) for intelligent filtering and summarization.

## Features

- Searcher Agent: Queries arXiv across specific health and AI/ML categories (q-bio, physics.med-ph, stat.AP, cs.AI, cs.LG).
- Ranking Agent: Uses Gemma 3 1B to evaluate and score papers based on their relevance to healthcare applications and user queries.
- Summarizer Agent: Generates concise, bulleted summaries of key findings from paper abstracts.
- Vector Store: Persists key findings and summaries using ChromaDB for later retrieval.
- Interactive UI: A Streamlit interface with session state persistence and ranking toggles.

## Prerequisites

- Python 3.10 or higher
- Ollama installed and running
- Gemma 3 1B model downloaded (run: ollama pull gemma3:1b)

## Installation

1. Clone the repository and navigate to the project folder.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Ollama service in a separate terminal:
   ```bash
   ollama serve
   ```
2. Launch the AutoScholar dashboard:
   ```bash
   streamlit run app.py
   ```
3. Enter a research topic (e.g., "Deep Learning in Cardiology") and select your preferred ranking method.

## Architecture

The project is structured as follows:
- agents/searcher.py: Categorical arXiv retrieval logic.
- agents/summarizer.py: Gemma-powered ranking and summarization.
- database/vector_store.py: ChromaDB persistence layer.
- app.py: Streamlit frontend and state management.
- docs/implementation_plan.md: Original design and roadmap.
- AGENTS.md: Documentation on agent roles and instructions.
