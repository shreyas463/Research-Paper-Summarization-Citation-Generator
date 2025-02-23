export interface Paper {
    title: string;
    authors: string[];
    abstract: string;
    url: string;
    published_date: string;
    citation?: string;
    source?: string;
}

export interface PaperSummary {
    paper_id: string;
    summary: string;
    key_points: string[];
    citation: string;
}

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function searchPapers(query: string, maxResults: number = 5): Promise<Paper[]> {
    const response = await fetch(`${API_BASE_URL}/api/search`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query, max_results: maxResults }),
    });

    if (!response.ok) {
        throw new Error('Failed to search papers');
    }

    return response.json();
}

export async function generateSummary(paper: Paper): Promise<PaperSummary> {
    const response = await fetch(`${API_BASE_URL}/api/summarize`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(paper),
    });

    if (!response.ok) {
        throw new Error('Failed to generate summary');
    }

    return response.json();
}

export async function generateCitation(paper: Paper, style: string = 'apa'): Promise<string> {
    const response = await fetch(`${API_BASE_URL}/api/generate-citation?style=${style}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(paper),
    });

    if (!response.ok) {
        throw new Error('Failed to generate citation');
    }

    const data = await response.json();
    return data.citation;
} 