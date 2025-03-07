# Quick Start Guide

This guide provides the fastest path to get the Research Paper Summarization & Citation Generator up and running for development.

## Prerequisites

Ensure you have the following installed:
- Python 3.9+
- Node.js v18+
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/research-paper-summarization-citation-generator.git
cd research-paper-summarization-citation-generator
```

## Step 2: Set Up API Keys

You'll need the following API keys:

1. **OpenAI API Key**: Get one at [platform.openai.com](https://platform.openai.com/)
2. **Pinecone API Key**: Sign up at [pinecone.io](https://www.pinecone.io/)
3. **Semantic Scholar API Key**: Register at [semanticscholar.org/product/api](https://www.semanticscholar.org/product/api)

## Step 3: Set Up Pinecone Index

1. Log in to your Pinecone dashboard
2. Create a new index:
   - Name: `research_papers`
   - Dimensions: `1536`
   - Metric: `cosine`
3. Note your API key and environment

## Step 4: Configure Backend

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
```

Edit the `.env` file and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_api_key
```

## Step 5: Configure Frontend

```bash
cd ../frontend

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env.local
```

## Step 6: Start the Application

### Terminal 1: Start the Backend
```bash
cd backend
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
uvicorn main:app --reload
```

### Terminal 2: Start the Frontend
```bash
cd frontend
npm run dev
```

## Step 7: Access the Application

Open your browser and navigate to:
- Application: [http://localhost:3000](http://localhost:3000)
- API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

## Common Issues

If you encounter problems:
1. Check the [Troubleshooting Guide](TROUBLESHOOTING.md)
2. Ensure all API keys are correctly set
3. Verify the Pinecone index is properly configured

## Next Steps

Once you have the application running:
1. Try searching for papers on a research topic
2. Generate summaries for papers of interest
3. Explore the API documentation to understand available endpoints
4. Check the [Development Roadmap](ROADMAP.md) for areas to contribute

## Development Workflow

1. Create a feature branch for your work
2. Make your changes
3. Test thoroughly
4. Submit a pull request

For more detailed information, see the [Contributing Guide](CONTRIBUTING.md). 