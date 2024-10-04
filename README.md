# Sorting Visualizer with Explanations

This is a Sorting Visualizer web application that helps users understand the step-by-step process of various sorting algorithms. The app uses **Next.js** for the frontend and **Django** for the backend. It visualizes how sorting algorithms like Bubble Sort, Insertion Sort, Merge Sort, and Quick Sort work, providing explanations at each step of the process.

## Features

- **Sorting Algorithms**: Includes visualizations and step-by-step explanations for the following sorting algorithms:
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
- **Step Navigation**: Allows users to navigate through each sorting step using "Next Step" and "Previous Step" buttons.
- **Random Array Generation**: A button that generates a random array of numbers for testing.
- **Light/Dark Theme**: Users can toggle between light and dark themes.
- **Explanations**: For each step of the sorting process, a detailed explanation is provided on what the algorithm is doing.

## Technologies Used

- **Frontend**: Next.js (React) with TypeScript
- **Backend**: Django (Python) with Django REST Framework (DRF)
- **Styling**: CSS

## Project Setup

### Prerequisites

Before you begin, ensure you have the following tools installed on your system:

- Node.js
- Python 3.x
- Django

### Backend Setup (Django)

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the backend directory:

    ```bash
    cd backend
    ```

3. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate  # For Windows
    ```

4. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

The backend will now be running on `http://127.0.0.1:8000`.

### Frontend Setup (Next.js)

1. Navigate to the frontend directory:

    ```bash
    cd frontend
    ```

2. Install the required Node.js dependencies:

    ```bash
    npm install
    ```

3. Run the Next.js development server:

    ```bash
    npm run dev
    ```

The frontend will now be running on `http://localhost:3000`.

## Usage

1. Enter an array of numbers separated by commas (e.g., `3,8,2,5`).
2. Select a sorting algorithm from the dropdown menu.
3. Click the **Sort** button to start the visualization.
4. Use the **Next Step** and **Previous Step** buttons to navigate through the sorting process step-by-step.
5. Click the **Randomize** button to generate a random array for testing.
6. Toggle between **Light Mode** and **Dark Mode** using the provided button.


