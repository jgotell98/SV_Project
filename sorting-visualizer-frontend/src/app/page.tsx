// pages/index.tsx
"use client"; // Mark the file as a Client Component

import React, { useState, useEffect } from 'react';

const HomePage = () => {
    const [theme, setTheme] = useState<'light' | 'dark'>('light');
    const [inputArray, setInputArray] = useState<string>(''); 
    const [algorithm, setAlgorithm] = useState<string>('bubble_sort');
    const [steps, setSteps] = useState<number[][]>([]);
    const [explanations, setExplanations] = useState<string[]>([]);  // Explanations for each step
    const [currentStep, setCurrentStep] = useState<number>(0);

    // Fetch sorting steps and explanations from Django backend
    const fetchSortSteps = async () => {
        const formattedArray: number[] = inputArray.split(',').map(Number);
        const res = await fetch('http://127.0.0.1:8000/api/sort/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ array: formattedArray, algorithm }),
        });
        
        if (res.ok) {
            const data = await res.json();
            setSteps(data.steps);
            setExplanations(data.explanations);  // Get explanations for each step
            setCurrentStep(0);
        } else {
            console.error('Error fetching sorting steps:', res.statusText);
        }
    };

    // Generate a random array of numbers
    const generateRandomArray = () => {
        const randomArray = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100));  // Array of 10 random numbers (0-99)
        setInputArray(randomArray.join(','));  // Update input array with random numbers as a string
    };

    // Go to the next step
    const handleNextStep = () => {
        if (currentStep < steps.length - 1) {
            setCurrentStep(currentStep + 1);
        }
    };

    // Go to the previous step
    const handlePreviousStep = () => {
        if (currentStep > 0) {
            setCurrentStep(currentStep - 1);
        }
    };

    // Toggle between light and dark mode
    const toggleTheme = () => {
        setTheme(theme === 'light' ? 'dark' : 'light');
    };

    return (
        <div className={theme}>
            <main className="container">
                <h1>Sorting Visualizer</h1>

                {/* Input Array and Algorithm Selection */}
                <div className="controls">
                    <input
                        type="text"
                        placeholder="Enter numbers separated by commas"
                        value={inputArray}
                        onChange={(e) => setInputArray(e.target.value)}
                    />
                    <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value)}>
                        <option value="bubble_sort">Bubble Sort</option>
                        <option value="insertion_sort">Insertion Sort</option>
                        <option value="merge_sort">Merge Sort</option>
                        <option value="quicksort">Quick Sort</option>
                    </select>
                    <button onClick={fetchSortSteps}>Sort</button>
                    <button onClick={generateRandomArray}>Randomize</button> {/* Randomize Button */}
                </div>

                {/* Display Sorted Array */}
                <div className="array-container">
                    {steps[currentStep]?.map((num, index) => (
                        <div key={index} className="array-bar">
                            {num}
                        </div>
                    ))}
                </div>

                {/* Step Controls and Theme Toggle */}
                <div className="controls">
                    <button onClick={handlePreviousStep}>Previous Step</button>
                    <button onClick={handleNextStep}>Next Step</button>
                    <button onClick={toggleTheme}>
                        Switch to {theme === 'light' ? 'Dark' : 'Light'} Mode
                    </button>
                </div>

                {/* Explanation of Current Step */}
                <div className="explanation">
                    <p>{`Current Step: ${currentStep + 1} of ${steps.length}`}</p>
                    <p>{`Explanation: ${explanations[currentStep]}`}</p>
                </div>
            </main>
        </div>
    );
};

export default HomePage;


