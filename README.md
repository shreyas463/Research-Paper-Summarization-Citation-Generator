# AI-Powered Research Paper Summarization & Citation Generator

## Overview
This tool helps researchers efficiently process academic literature by:
- Automatically fetching papers from arXiv, PubMed, and Google Scholar
- Generating concise summaries using advanced NLP techniques
- Creating properly formatted citations
- Providing context-aware paper recommendations
- Learning from user feedback to improve results

## Features
- 🔍 Multi-source paper search and retrieval
- 📝 AI-powered paper summarization
- ✍️ Automated citation generation
- 🤖 RAG-based contextual recommendations
- 📊 Continuous learning from user feedback
- 📚 Citation impact tracking

## Project Status

This project is currently in the **foundation stage**. The basic structure and core functionality have been implemented, but there are many opportunities for enhancement and expansion. We welcome contributors to help build upon this foundation.

**Key Documentation for Contributors:**
- [Quick Start Guide](QUICKSTART.md) - Get up and running quickly
- [Contributing Guide](CONTRIBUTING.md) - How to contribute to this project
- [Development Roadmap](ROADMAP.md) - Planned features and enhancements
- [Troubleshooting Guide](TROUBLESHOOTING.md) - Solutions for common issues

## Tech Stack
- Frontend: Next.js with TypeScript
- Backend: Python FastAPI
- ML/NLP: Transformers, LangChain
- Vector Database: Pinecone
- API Integration: arXiv, PubMed, Semantic Scholar

## Getting Started

For the fastest setup, see the [Quick Start Guide](QUICKSTART.md).

### Prerequisites
- Node.js (v18 or higher)
- Python 3.9+
- pip
- yarn or npm

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/research-paper-summarization-citation-generator.git
cd research-paper-summarization-citation-generator
```

2. Set up the frontend
```bash
cd frontend
yarn install
cp .env.example .env.local  # Configure your environment variables
```

3. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # Configure your environment variables
```

### Environment Variables

#### Backend (.env)
You'll need to obtain API keys for the following services:
- OpenAI API (for GPT-4 and embeddings)
- Pinecone (for vector database)
- Semantic Scholar API
- PubMed API (optional)

Configure these in `backend/.env`:
```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_api_key
PUBMED_API_KEY=your_pubmed_api_key
```

#### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Running the Application

1. Start the backend server
```bash
cd backend
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
uvicorn main:app --reload
```

2. Start the frontend development server
```bash
cd frontend
yarn dev
```

The application will be available at http://localhost:3000

## Setting Up Pinecone Vector Database

1. Create a Pinecone account at [pinecone.io](https://www.pinecone.io/)
2. Create a new index with the following configuration:
   - Name: `research_papers`
   - Dimensions: `1536` (for text-embedding-ada-002)
   - Metric: `cosine`
3. Copy your API key and environment from the Pinecone dashboard
4. Add these to your `.env` file

## API Documentation

The backend API documentation is available at http://localhost:8000/docs when the server is running.

### Available Endpoints

- `POST /api/search`: Search for papers across multiple sources
- `POST /api/summarize`: Generate paper summary using RAG
- `POST /api/generate-citation`: Generate citation in specified format

## Future Development

This project has significant potential for expansion. See the [Development Roadmap](ROADMAP.md) for planned features and enhancements. Key areas for future development include:

1. **Enhanced Paper Retrieval** - Support for more academic sources and full-text analysis
2. **Improved Summarization** - Section-by-section summarization and domain-specific knowledge
3. **User Management** - Authentication, profiles, and saved papers
4. **Advanced UI** - Mobile responsiveness, dark mode, and accessibility features
5. **Research Analytics** - Citation graphs and trend analysis

## Contributing

We welcome contributions from developers of all skill levels! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

If you encounter any issues, check the [Troubleshooting Guide](TROUBLESHOOTING.md) for solutions to common problems.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- arXiv API for paper access
- Semantic Scholar API for academic paper data
- OpenAI for language models
- Pinecone for vector search capabilities
