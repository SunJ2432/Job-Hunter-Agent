// user interface events and results from prompt

import { useRef, useState, useEffect } from 'react';  // import React state management hook
import axios from 'axios';  // import Axios for making HTTP requests
import React from 'react';

export default function Input() {
    // state to store the user input
   const [prompt, setPrompt] = useState(' ');
   const [loading, setLoading] = useState(false);
   const [table, setTable] = useState<any[]>([]);
    

    // input sanitization helper
    function isValidPrompt(text: string): boolean {
        return text.trim().length > 0;
    }

    // function to handle form submission
    const handleSubmit = async (e: React.FormEvent) => {
        // prevent page reload on form submission
        e.preventDefault();
        const sanitized = prompt.trim();

        if (!isValidPrompt(sanitized)) {
            alert('prompt cannot be empty or whitespace.');
            return;
        }
        setLoading(true);
        setTable([]);
        // try {

        // }

    };

    return (
        <div className="text-left w-full">
            <form onSubmit={handleSubmit} className="rounded mb-6">
                <input type="text" value={prompt} 
                // Input field where user type their prompt 
                placeholder="Search job title..."
                // update input state
                onChange={(e) => setPrompt(e.target.value)}
                className="border border-gray-300 rounded mb-2" />
                <button type="submit"
                className="bg-green-300 text-white px-4 py-2 rounded hover:bg-green-500">Search</button>
            </form>
            {loading && <p className="text-black-300 font-bold">Loading jobs...</p>}

        </div>
        
    );
       
}


