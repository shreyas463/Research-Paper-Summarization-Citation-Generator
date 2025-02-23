import { Paper, PaperSummary } from '@/lib/api';
import { useState } from 'react';

interface PaperCardProps {
    paper: Paper;
    onGenerateSummary: (paper: Paper) => Promise<void>;
    summary?: PaperSummary;
    isLoading?: boolean;
}

export default function PaperCard({
    paper,
    onGenerateSummary,
    summary,
    isLoading = false,
}: PaperCardProps) {
    const [isExpanded, setIsExpanded] = useState(false);

    return (
        <div className="w-full p-6 bg-white rounded-lg shadow-md mb-4">
            <div className="flex justify-between items-start">
                <div>
                    <h3 className="text-xl font-semibold text-gray-900 mb-2">
                        {paper.title}
                    </h3>
                    <p className="text-sm text-gray-600 mb-2">
                        {paper.authors.join(', ')} • {paper.published_date}
                    </p>
                    <p className="text-sm text-gray-500 mb-2">
                        Source: {paper.source}
                    </p>
                </div>
                <button
                    onClick={() => setIsExpanded(!isExpanded)}
                    className="text-blue-500 hover:text-blue-600"
                >
                    {isExpanded ? 'Show Less' : 'Show More'}
                </button>
            </div>

            {isExpanded && (
                <div className="mt-4">
                    <h4 className="font-semibold text-gray-900 mb-2">Abstract</h4>
                    <p className="text-gray-700 mb-4">{paper.abstract}</p>

                    {!summary && !isLoading && (
                        <button
                            onClick={() => onGenerateSummary(paper)}
                            className="px-4 py-2 bg-green-500 text-white rounded-md hover:bg-green-600"
                        >
                            Generate Summary
                        </button>
                    )}

                    {isLoading && (
                        <div className="flex items-center text-gray-600">
                            <svg className="animate-spin h-5 w-5 mr-2" viewBox="0 0 24 24">
                                <circle
                                    className="opacity-25"
                                    cx="12"
                                    cy="12"
                                    r="10"
                                    stroke="currentColor"
                                    strokeWidth="4"
                                />
                                <path
                                    className="opacity-75"
                                    fill="currentColor"
                                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                                />
                            </svg>
                            Generating summary...
                        </div>
                    )}

                    {summary && (
                        <div className="mt-4">
                            <h4 className="font-semibold text-gray-900 mb-2">Summary</h4>
                            <p className="text-gray-700 mb-4">{summary.summary}</p>

                            <h4 className="font-semibold text-gray-900 mb-2">Key Points</h4>
                            <ul className="list-disc list-inside mb-4">
                                {summary.key_points.map((point, index) => (
                                    <li key={index} className="text-gray-700">
                                        {point}
                                    </li>
                                ))}
                            </ul>

                            <h4 className="font-semibold text-gray-900 mb-2">Citation</h4>
                            <p className="text-gray-700 p-4 bg-gray-50 rounded-md font-mono text-sm">
                                {summary.citation}
                            </p>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
} 