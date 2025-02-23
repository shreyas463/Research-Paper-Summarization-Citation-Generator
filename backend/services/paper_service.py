import arxiv
from scholarly import scholarly
import requests
from typing import List, Dict, Any
import os
from datetime import datetime

class PaperService:
    def __init__(self):
        self.semantic_scholar_api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
        self.pubmed_api_key = os.getenv("PUBMED_API_KEY")

    async def search_arxiv(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Search papers on arXiv
        """
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        papers = []
        async for result in search.results():
            papers.append({
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "abstract": result.summary,
                "url": result.pdf_url,
                "published_date": result.published.strftime("%Y-%m-%d"),
                "source": "arxiv"
            })
        return papers

    async def search_semantic_scholar(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Search papers on Semantic Scholar
        """
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        headers = {"x-api-key": self.semantic_scholar_api_key}
        params = {
            "query": query,
            "limit": max_results,
            "fields": "title,authors,abstract,url,year"
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            return []

        papers = []
        for paper in response.json().get("data", []):
            papers.append({
                "title": paper.get("title", ""),
                "authors": [author.get("name", "") for author in paper.get("authors", [])],
                "abstract": paper.get("abstract", ""),
                "url": paper.get("url", ""),
                "published_date": str(paper.get("year", "")),
                "source": "semantic_scholar"
            })
        return papers

    async def search_google_scholar(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Search papers on Google Scholar
        """
        search_query = scholarly.search_pubs(query)
        papers = []
        try:
            for _ in range(max_results):
                result = next(search_query)
                paper = {
                    "title": result.bib.get("title", ""),
                    "authors": result.bib.get("author", "").split(" and "),
                    "abstract": result.bib.get("abstract", ""),
                    "url": result.bib.get("url", ""),
                    "published_date": result.bib.get("year", ""),
                    "source": "google_scholar"
                }
                papers.append(paper)
        except StopIteration:
            pass
        return papers

    async def search_all_sources(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Search papers across all available sources
        """
        results = []
        
        # Search in parallel (to be implemented)
        arxiv_results = await self.search_arxiv(query, max_results)
        semantic_scholar_results = await self.search_semantic_scholar(query, max_results)
        google_scholar_results = await self.search_google_scholar(query, max_results)

        # Combine and deduplicate results
        results.extend(arxiv_results)
        results.extend(semantic_scholar_results)
        results.extend(google_scholar_results)

        # Remove duplicates based on title
        seen_titles = set()
        unique_results = []
        for paper in results:
            if paper["title"].lower() not in seen_titles:
                seen_titles.add(paper["title"].lower())
                unique_results.append(paper)

        return unique_results[:max_results] 