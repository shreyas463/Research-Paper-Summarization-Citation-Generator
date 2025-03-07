# Contributing to the Research Paper Summarization & Citation Generator

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for developers who want to continue building and improving this application.

## Project Overview

This project is an AI-powered tool that helps researchers find, summarize, and cite academic papers. It uses:
- FastAPI backend with Python
- Next.js frontend with TypeScript and Tailwind CSS
- OpenAI's models for summarization and embeddings
- Pinecone for vector storage
- Integration with academic paper sources (arXiv, Semantic Scholar, Google Scholar)

## Development Setup

### Prerequisites

- Python 3.9+
- Node.js v18+
- API keys for:
  - OpenAI
  - Pinecone
  - Semantic Scholar
  - PubMed (optional)

### Getting Started

1. Clone the repository
2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env  # Then edit with your API keys
   ```
3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   cp .env.example .env.local
   ```

## Project Structure

### Backend

- `main.py`: FastAPI application entry point
- `services/`: Core functionality modules
  - `paper_service.py`: Paper search and retrieval
  - `summarization_service.py`: RAG-based summarization

### Frontend

- `src/app/`: Next.js pages
- `src/components/`: Reusable UI components
- `src/lib/`: Utility functions and API client

## Roadmap and Future Improvements

### Backend Enhancements

1. **Improved Paper Retrieval**
   - Add support for more academic sources
   - Implement PDF parsing for full-text analysis
   - Add caching for frequently accessed papers

2. **Enhanced Summarization**
   - Implement section-by-section summarization
   - Add support for different summary lengths
   - Incorporate domain-specific knowledge

3. **Citation Management**
   - Support more citation styles (MLA, Chicago, etc.)
   - Add bibliography generation
   - Implement citation validation

4. **User Management**
   - Add authentication
   - Implement user profiles
   - Add saved papers and summaries

### Frontend Enhancements

1. **UI Improvements**
   - Add dark mode
   - Implement responsive design for mobile
   - Add accessibility features

2. **User Experience**
   - Add paper comparison feature
   - Implement drag-and-drop for PDF uploads
   - Add export functionality for summaries and citations

3. **Visualization**
   - Add citation graphs
   - Implement paper relationship visualization
   - Add trend analysis for research topics

## Testing

- Add unit tests for backend services
- Implement integration tests for API endpoints
- Add frontend component tests
- Set up end-to-end testing

## Deployment

- Add Docker configuration
- Set up CI/CD pipeline
- Implement monitoring and logging
- Add performance optimization

## Code Style and Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for TypeScript/JavaScript
- Write meaningful commit messages
- Document all functions and classes

## Getting Help

If you have questions or need assistance, please:
1. Check existing issues
2. Create a new issue with a detailed description
3. Reference relevant documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details. 