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

## Tech Stack
- Frontend: Next.js with TypeScript
- Backend: Python FastAPI
- ML/NLP: Transformers, LangChain
- Vector Database: Pinecone
- API Integration: arXiv, PubMed, Semantic Scholar

## Getting Started

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
```

3. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
```
Edit .env with your API keys and configuration

### Running the Application

1. Start the backend server
```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend development server
```bash
cd frontend
yarn dev
```

The application will be available at http://localhost:3000

## Contributing
Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
