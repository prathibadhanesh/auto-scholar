import ollama

class SummarizerAgent:
    def __init__(self, model="gemma3:1b"):
        self.model = model

    def summarize(self, text, context=""):
        prompt = f"""
        You are a specialized health research assistant. 
        Your task is to summarize the following medical literature snippet accurately and concisely.
        
        Context/Topic: {context}
        
        Snippet: {text}
        
        Please provide a bulleted summary of key findings.
        """
        
        response = ollama.chat(model=self.model, messages=[
            {'role': 'user', 'content': prompt}
        ])
        return response['message']['content']
        
    def rank_papers(self, query, papers):
        if not papers:
            return []
            
        ranked_results = []
        for paper in papers:
            prompt = f"""
            You are a computer science researcher focusing on healthcare related research, score the following paper's relevance to the computer science or AI/ML applications in the healthcare domain of the query: "{query}".
            
            Title: {paper['title']}
            Abstract: {paper['summary']}
            
            SCORING RULES:
            1. **Medical Context**: Direct medical, biological, or clinical research is highly relevant.
            2. **Applied AI/ML**: Computer Science or Machine Learning papers (e.g., from arXiv cs.LG or cs.AI) are HIGHLY RELEVANT if they are applied to healthcare, clinical diagnostics, or medical data. 
            3. **Irrelevance**: Purely theoretical CS/Physics/Math with no healthcare application should be scored low.
            4. **Query Match**: How specifically does it address "{query}"?
            
            Output: Return ONLY the integer score (0 to 10).
            Score:"""
            
            try:
                response = ollama.chat(model=self.model, messages=[
                    {'role': 'user', 'content': prompt}
                ])
                score_str = response['message']['content'].strip()
                # Extract first digit found
                import re
                match = re.search(r'\d+', score_str)
                score = int(match.group()) if match else 0
            except:
                score = 0
                
            paper['score'] = score
            ranked_results.append(paper)
            
        # Sort by score descending
        ranked_results.sort(key=lambda x: x['score'], reverse=True)
        return ranked_results

if __name__ == "__main__":
    summarizer = SummarizerAgent()
    test_text = "Clinical trials show that Vitamin D supplementation can improve bone density in elderly patients."
    print(summarizer.summarize(test_text, "Vitamin D benefits"))
