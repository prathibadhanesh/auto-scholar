# AutoScholar Agent Documentation

## Overview
AutoScholar utilizes a multi-agent approach to handle the complexity of medical literature research. The agents coordinate to move from broad data discovery to specific insight extraction.

## Agent Descriptions

### Searcher Agent (agents/searcher.py)
- Role: Data Discovery
- Capability: Interface with the arXiv API.
- Categories: Restricts searches to q-bio.*, physics.med-ph, stat.AP, cs.AI, and cs.LG to ensure health-related or applied-AI-in-health results.
- Logic: Combines user queries with categorical filters to maximize precision.

### Summarizer & Ranking Agent (agents/summarizer.py)
- Role: Evaluation and Synthesis
- Capability: Interfaces with Ollama (Gemma 3 1B).
- Ranking: Scores papers from 0-10 based on their application to the healthcare domain.
- Summarization: Transforms dense abstracts into actionable, bulleted summaries.

## Instructions for Development
1. For every functionality created, ensure documentation is stored in the docs subfolder in markdown format.
2. Activate the virtual environment before executing any python script.
3. Always commit changes to the local git repository.