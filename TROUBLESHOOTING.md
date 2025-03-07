# Troubleshooting Guide

This document provides solutions for common issues you might encounter when setting up or developing the Research Paper Summarization & Citation Generator.

## API and Authentication Issues

### OpenAI API Issues

**Issue**: `Error: Authentication failed with OpenAI API`

**Solutions**:
1. Verify your OpenAI API key is correctly set in the `.env` file
2. Check if your OpenAI account has sufficient credits
3. Ensure you're using the correct API version
4. Check if your API key has the necessary permissions

### Pinecone Issues

**Issue**: `Error: Failed to initialize Pinecone index`

**Solutions**:
1. Verify your Pinecone API key and environment are correctly set in the `.env` file
2. Ensure you've created an index named "research_papers" in your Pinecone dashboard
3. Check if your Pinecone plan supports the dimensions you're using (1024 for text-embedding-ada-002)
4. Verify your index is using "cosine" as the metric type

**Issue**: `Error: No records found in Pinecone index`

**Solutions**:
1. Make sure you've successfully stored embeddings in the index
2. Check if the index name in your code matches the one in Pinecone dashboard
3. Verify the namespace parameter if you're using namespaces

### Semantic Scholar API Issues

**Issue**: `Error: Rate limit exceeded for Semantic Scholar API`

**Solutions**:
1. Implement rate limiting in your code (e.g., add delays between requests)
2. Consider caching results to reduce API calls
3. Contact Semantic Scholar for a higher rate limit if needed

## Backend Issues

### Installation Problems

**Issue**: `Error: Module not found`

**Solutions**:
1. Verify you've activated the virtual environment
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Check if the package is correctly imported in your code

### Runtime Errors

**Issue**: `Error: Async for loop not working with arxiv library`

**Solutions**:
1. Make sure you're using the correct version of the arxiv library
2. Consider using a synchronous approach with the arxiv library
3. Implement a wrapper that converts synchronous calls to async

**Issue**: `Error: Connection refused when connecting to backend`

**Solutions**:
1. Verify the backend server is running
2. Check if the port (default: 8000) is available and not blocked by firewall
3. Ensure the host is correctly set (0.0.0.0 for network access)

## Frontend Issues

### Build Errors

**Issue**: `Error: TypeScript compilation failed`

**Solutions**:
1. Check for type errors in your code
2. Ensure all required type definitions are installed
3. Run `npm install --save-dev @types/react @types/react-dom` if needed

### Runtime Errors

**Issue**: `Error: Failed to fetch data from API`

**Solutions**:
1. Verify the backend server is running
2. Check if the API URL is correctly set in `.env.local`
3. Inspect network requests in browser developer tools for more details
4. Ensure CORS is properly configured on the backend

**Issue**: `Error: Component rendering issues`

**Solutions**:
1. Check for null or undefined values in your component props
2. Implement proper loading states
3. Use React DevTools to inspect component state and props

## Environment Setup Issues

**Issue**: `Error: Python virtual environment not working`

**Solutions**:
1. Ensure you have Python 3.9+ installed
2. Try creating a new virtual environment: `python -m venv venv_new`
3. On Windows, you might need to adjust execution policies: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

**Issue**: `Error: Node.js dependencies not installing`

**Solutions**:
1. Clear npm cache: `npm cache clean --force`
2. Delete node_modules folder and reinstall: `rm -rf node_modules && npm install`
3. Ensure you're using Node.js v18+

## Pinecone Vector Database Setup

**Issue**: Creating and configuring the Pinecone index

**Solutions**:
1. Log in to your Pinecone dashboard
2. Create a new index with the following configuration:
   - Name: `research_papers`
   - Dimensions: `1536` (for text-embedding-ada-002)
   - Metric: `cosine`
   - Pod Type: Choose based on your needs (e.g., s1 for development)
3. After creation, note your API key and environment

## Common Code Modifications

### Changing the Embedding Model

If you want to use a different embedding model:

1. Update the `EMBEDDING_MODEL` in your `.env` file
2. Ensure the Pinecone index dimensions match your new model's output dimensions
3. Update the embedding initialization in `summarization_service.py`

### Adding a New Paper Source

To add a new academic paper source:

1. Create a new method in `paper_service.py` (e.g., `search_ieee`)
2. Add the API key to your `.env` file if needed
3. Update the `search_all_sources` method to include your new source
4. Add proper error handling and rate limiting

## Getting Additional Help

If you're still experiencing issues:

1. Check the project's GitHub Issues page
2. Search for similar problems in Stack Overflow
3. Consult the documentation for the specific library causing issues
4. Create a new issue with detailed information about your problem, including:
   - Error messages
   - Environment details
   - Steps to reproduce
   - Code snippets 