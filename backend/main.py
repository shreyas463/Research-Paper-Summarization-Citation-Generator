from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

from services.paper_service import PaperService
from services.summarization_service import SummarizationService

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Research Paper Assistant API",
    description="API for paper summarization and citation generation",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
paper_service = PaperService()
summarization_service = SummarizationService()

# Pydantic models for request/response
class PaperQuery(BaseModel):
    query: str
    max_results: Optional[int] = 5

class Paper(BaseModel):
    title: str
    authors: List[str]
    abstract: str
    url: str
    published_date: str
    citation: Optional[str] = None
    source: Optional[str] = None

class PaperSummary(BaseModel):
    paper_id: str
    summary: str
    key_points: List[str]
    citation: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Research Paper Assistant API"}

@app.post("/api/search", response_model=List[Paper])
async def search_papers(query: PaperQuery):
    """
    Search for papers across multiple sources (arXiv, PubMed, Google Scholar)
    """
    try:
        papers = await paper_service.search_all_sources(
            query=query.query,
            max_results=query.max_results
        )
        return papers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/summarize", response_model=PaperSummary)
async def summarize_paper(paper: Paper):
    """
    Generate a summary of the paper using RAG
    """
    try:
        summary = await summarization_service.generate_summary(paper.dict())
        # Store paper embedding for future reference
        await summarization_service.store_paper_embedding(paper.dict())
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-citation")
async def generate_citation(paper: Paper, style: str = "apa"):
    """
    Generate citation in specified format
    """
    try:
        citation = await summarization_service.generate_citation(paper.dict(), style)
        return {"citation": citation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("BACKEND_PORT", 8000))) 