import streamlit as st
from agents.searcher import SearcherAgent
from agents.summarizer import SummarizerAgent
from database.vector_store import VectorStore

# Initialize components
@st.cache_resource
def init_components():
    return SearcherAgent(), SummarizerAgent(), VectorStore()

searcher, summarizer, vector_store = init_components()

st.set_page_config(page_title="AutoScholar: Health Research Agent", layout="wide")

st.title("AutoScholar: Health Research Agent")
st.markdown("---")

# Initialize session state
if 'papers' not in st.session_state:
    st.session_state.papers = []
if 'last_query' not in st.session_state:
    st.session_state.last_query = ""

query = st.text_input("Enter a medical or health research topic:", 
                     value=st.session_state.last_query,
                     placeholder="e.g., impact of Vitamin D on immune system")

col1, col2 = st.columns(2)
with col1:
    ranking_method = st.radio("Ranking Method:", ["ArXiv Default", "LLM-based Re-ranking"], horizontal=True)
with col2:
    max_res = st.slider("Max Results:", 2, 10, 5)

if st.button("Search & Summarize"):
    if query:
        st.session_state.last_query = query
        with st.spinner("Searching arXiv for papers in health categories..."):
            fetch_count = max_res * 2 if ranking_method == "LLM-based Re-ranking" else max_res
            papers = searcher.search_papers(query, max_results=fetch_count)
        
        if not papers:
            st.warning("No papers found for this topic in health categories.")
            st.session_state.papers = []
        else:
            if ranking_method == "LLM-based Re-ranking":
                with st.spinner("Re-ranking papers with Gemma3..."):
                    papers = summarizer.rank_papers(query, papers)
                    papers = [p for p in papers if p.get('score', 0) >= 4][:max_res]
            else:
                papers = papers[:max_res]
            
            st.session_state.papers = papers

# Display results from session state
if st.session_state.papers:
    st.subheader(f"Results for: {st.session_state.last_query}")
    for paper in st.session_state.papers:
        score_info = f" [Health Score: {paper['score']}/10]" if 'score' in paper else ""
        with st.expander(f"📄 {paper['title']} ({paper['published']}){score_info}"):
            st.write(paper['summary'])
            categories = paper.get('categories', [])
            st.markdown(f"**Categories**: {', '.join(categories) if categories else 'N/A'}")
            st.markdown(f"[View Full PDF]({paper['url']})")
            
            # Using a unique key for each summary in session state if needed, 
            # but for now we just display the summary result below the button
            if st.button(f"Summarize this paper", key=f"sum_{paper['url']}"):
                with st.spinner("Summarizing..."):
                    summary = summarizer.summarize(paper['summary'], st.session_state.last_query)
                    st.info(summary)
                    
                    # Store in vector database
                    vector_store.add_documents(
                        [summary],
                        [{"title": paper['title'], "url": paper['url'], "query": st.session_state.last_query, "score": paper.get('score', 0)}]
                    )
                    st.success("Summary saved to Vector Store!")

st.sidebar.header("Recent Findings")
if st.sidebar.button("Retrieve Stored Findings"):
    hist_query = query if query else "latest research"
    history = vector_store.query(hist_query, n_results=3)
    if history and history['documents']:
        for i, doc in enumerate(history['documents'][0]):
            st.sidebar.markdown(f"**Result {i+1}**")
            st.sidebar.write(doc)
            st.sidebar.markdown("---")
    else:
        st.sidebar.info("No stored findings found.")
