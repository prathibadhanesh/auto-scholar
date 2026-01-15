import arxiv
import os

class SearcherAgent:
    def __init__(self):
        self.client = arxiv.Client()

    def search_papers(self, query, max_results=10, categories=None):
        if categories is None:
            # Expanded health-related categories including AI/ML applications
            categories = ['q-bio.*', 'physics.med-ph', 'stat.AP', 'cs.AI', 'cs.LG']
        
        # Construct categorical query string
        cat_query = " OR ".join([f"cat:{cat}" for cat in categories])
        full_query = f"({query}) AND ({cat_query})"
        
        search = arxiv.Search(
            query=full_query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        
        results = []
        for result in self.client.results(search):
            paper_info = {
                "title": result.title,
                "summary": result.summary,
                "url": result.pdf_url,
                "published": result.published.strftime("%Y-%m-%d"),
                "categories": getattr(result, "categories", [])
            }
            results.append(paper_info)
        return results

if __name__ == "__main__":
    searcher = SearcherAgent()
    papers = searcher.search_papers("benefits of Vitamin D site:medrxiv.org OR site:biorxiv.org")
    for p in papers:
        print(f"Title: {p['title']}\nURL: {p['url']}\n")
