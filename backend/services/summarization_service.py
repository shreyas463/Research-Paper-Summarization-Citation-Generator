from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import pinecone
import os
from typing import List, Dict, Any

class SummarizationService:
    def __init__(self):
        # Initialize OpenAI
        self.llm = ChatOpenAI(
            model_name=os.getenv("SUMMARY_MODEL", "gpt-4"),
            temperature=float(os.getenv("TEMPERATURE", 0.7))
        )
        
        # Initialize Pinecone
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),
            environment=os.getenv("PINECONE_ENVIRONMENT")
        )
        
        # Initialize embeddings
        self.embeddings = OpenAIEmbeddings(
            model=os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
        )
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    async def generate_summary(self, paper: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a summary of the paper using RAG
        """
        # Create summary prompt
        summary_template = """
        You are an expert research paper summarizer. Given the following paper details,
        provide a comprehensive yet concise summary and extract key points.
        
        Title: {title}
        Authors: {authors}
        Abstract: {abstract}
        
        Please provide:
        1. A concise summary (2-3 paragraphs)
        2. 3-5 key points or findings
        3. Potential applications or implications
        
        Summary:
        """
        
        summary_prompt = PromptTemplate(
            input_variables=["title", "authors", "abstract"],
            template=summary_template
        )
        
        # Create summary chain
        summary_chain = LLMChain(
            llm=self.llm,
            prompt=summary_prompt
        )
        
        # Generate summary
        summary_result = await summary_chain.arun({
            "title": paper["title"],
            "authors": ", ".join(paper["authors"]),
            "abstract": paper["abstract"]
        })
        
        # Extract key points (simple implementation - can be enhanced)
        key_points = summary_result.split("\n\n")[1].split("\n")[1:]
        
        return {
            "paper_id": paper["url"],  # Using URL as paper ID for now
            "summary": summary_result.split("\n\n")[0],
            "key_points": key_points,
            "citation": await self.generate_citation(paper)
        }

    async def generate_citation(self, paper: Dict[str, Any], style: str = "apa") -> str:
        """
        Generate citation in the specified format
        """
        citation_template = """
        Generate a {style} citation for the following paper:
        
        Title: {title}
        Authors: {authors}
        Year: {year}
        URL: {url}
        
        Citation:
        """
        
        citation_prompt = PromptTemplate(
            input_variables=["style", "title", "authors", "year", "url"],
            template=citation_template
        )
        
        citation_chain = LLMChain(
            llm=self.llm,
            prompt=citation_prompt
        )
        
        citation_result = await citation_chain.arun({
            "style": style,
            "title": paper["title"],
            "authors": ", ".join(paper["authors"]),
            "year": paper["published_date"].split("-")[0] if "-" in paper["published_date"] else paper["published_date"],
            "url": paper["url"]
        })
        
        return citation_result.strip()

    async def store_paper_embedding(self, paper: Dict[str, Any]):
        """
        Store paper embeddings in Pinecone for future reference
        """
        # Combine paper information into a single text
        text = f"{paper['title']}\n{' '.join(paper['authors'])}\n{paper['abstract']}"
        
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Create and store embeddings
        vectorstore = Pinecone.from_texts(
            texts=chunks,
            embedding=self.embeddings,
            index_name=os.getenv("PINECONE_INDEX_NAME", "research_papers")
        )
        
        return vectorstore 