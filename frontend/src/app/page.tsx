'use client';

import { useState } from 'react';
import SearchBar from '@/components/SearchBar';
import PaperCard from '@/components/PaperCard';
import { Paper, PaperSummary, searchPapers, generateSummary } from '@/lib/api';

export default function Home() {
    const [papers, setPapers] = useState<Paper[]>([]);
    const [summaries, setSummaries] = useState<Record<string, PaperSummary>>({});
    const [isSearching, setIsSearching] = useState(false);
    const [isGeneratingSummary, setIsGeneratingSummary] = useState<Record<string, boolean>>({});
    const [error, setError] = useState<string | null>(null);

    const handleSearch = async (query: string) => {
        setIsSearching(true);
        setError(null);
        try {
            const results = await searchPapers(query);
            setPapers(results);
        } catch (err) {
            setError('Failed to search papers. Please try again.');
            console.error(err);
        } finally {
            setIsSearching(false);
        }
    };

    const handleGenerateSummary = async (paper: Paper) => {
        const paperId = paper.url;
        setIsGeneratingSummary(prev => ({ ...prev, [paperId]: true }));
        setError(null);
        try {
            const summary = await generateSummary(paper);
            setSummaries(prev => ({ ...prev, [paperId]: summary }));
        } catch (err) {
            setError('Failed to generate summary. Please try again.');
            console.error(err);
        } finally {
            setIsGeneratingSummary(prev => ({ ...prev, [paperId]: false }));
        }
    };

    return (
        <main className="min-h-screen bg-gray-50">
            <div className="container mx-auto px-4 py-8">
                <div className="text-center mb-8">
                    <h1 className="text-4xl font-bold text-gray-900 mb-4">
                        Research Paper Assistant
                    </h1>
                    <p className="text-lg text-gray-600 mb-8">
                        Search, summarize, and cite research papers with AI assistance
                    </p>
                    <div className="flex justify-center mb-8">
                        <SearchBar onSearch={handleSearch} isLoading={isSearching} />
                    </div>
                </div>

                {error && (
                    <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4">
                        {error}
                    </div>
                )}

                <div className="space-y-4">
                    {papers.map((paper) => (
                        <PaperCard
                            key={paper.url}
                            paper={paper}
                            onGenerateSummary={handleGenerateSummary}
                            summary={summaries[paper.url]}
                            isLoading={isGeneratingSummary[paper.url]}
                        />
                    ))}
                </div>

                {isSearching && papers.length === 0 && (
                    <div className="text-center text-gray-600 mt-8">
                        Searching for papers...
                    </div>
                )}

                {!isSearching && papers.length === 0 && (
                    <div className="text-center text-gray-600 mt-8">
                        No papers found. Try searching for a topic.
                    </div>
                )}
            </div>
        </main>
    );
}
