# E-Library Data Insights Dashboard

This project is a Python-based command-line tool to process, analyze, and visualize library borrowing data from a CSV file. It provides insights into book popularity, borrowing durations, and usage trends over time.

## Features

- **Data Loading & Cleaning**: Loads data from `library_transaction.csv` and handles missing or duplicate entries.
- **Statistical Analysis**: Calculates key metrics like the most popular book, average borrowing duration, and the busiest day of the week using **Pandas** and **NumPy**.
- **Data Visualization**: Generates several plots to visualize trends using **Matplotlib** and **Seaborn**:
  - A bar chart of the top 5 most borrowed books.
  - A pie chart showing the distribution of genres.
  - A line graph illustrating borrowing trends across months.
  - A heatmap showing borrowing activity by month and day of the week.

## Setup and Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <your-github-repo-link>
    cd <your-repo-name>
    ```

2.  **Install the required Python libraries:**
    Create a `requirements.txt` file with the following content:
    ```
    pandas
    numpy
    matplotlib
    seaborn
    ```
    Then, run the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  Make sure the `library_transaction.csv` file is in the same directory as the `library_dashboard.py` script.
2.  Run the script from your terminal:
    ```bash
    python library_dashboard.py
    ```
3.  The script will first print the calculated statistics to the console and then display the visualization plots one by one. Close each plot window to see the next one.
