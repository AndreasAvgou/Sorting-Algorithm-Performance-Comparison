# Sorting Algorithm Performance Comparison

This project benchmarks various sorting algorithms and stores the results in a PostgreSQL database. The application runs in a Docker environment and allows easy deployment and management of services.

## Project Overview

The goal of this project is to compare the performance of different sorting algorithms by measuring their execution time when sorting arrays of varying sizes. The results are stored in a PostgreSQL database, and the infrastructure is managed through Docker Compose.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Database Schema](#database-schema)
- [Future Improvements](#future-improvements)
- [License](#license)

## Technologies Used

- **Python** (Sorting algorithms and database interaction)
- **PostgreSQL** (Database for storing results)
- **Docker & Docker Compose** (Containerization and orchestration)
- **pgAdmin4** (Database management interface)

## Features

- Benchmarks multiple sorting algorithms:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort
  - Radix Sort
- Stores results in PostgreSQL
- Easy deployment with Docker Compose
- Includes pgAdmin4 for database management


## Directory Structure

- **`Dockerfile`**: Dockerfile for building the application container
- **`docker-compose.yml`**: Docker Compose configuration to manage the application and database containers
- **`init.sql`**: SQL file to initialize the PostgreSQL database schema
- **`main.py`**: Main Python script for executing the sorting benchmarks and storing results
- **`update_results_in_db.py`**: Python script to update the benchmark results into the database
- **`sorting_algorithms/`**: Directory containing implementations of various sorting algorithms
  - **`__init__.py`**: Empty file to make the `sorting_algorithms` directory a Python package
  - **`bubble_sort.py`**: Implementation of the Bubble Sort algorithm
  - **`selection_sort.py`**: Implementation of the Selection Sort algorithm
  - **`insertion_sort.py`**: Implementation of the Insertion Sort algorithm
  - **`merge_sort.py`**: Implementation of the Merge Sort algorithm
  - **`quick_sort.py`**: Implementation of the Quick Sort algorithm
  - **`heap_sort.py`**: Implementation of the Heap Sort algorithm
  - **`radix_sort.py`**: Implementation of the Radix Sort algorithm

## Installation and Setup

### Prerequisites

- **Docker**: For containerization.
- **Docker Compose**: For managing multi-container setups.
- **Power BI** (Optional): For data visualization performance.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AndreasAvgou/Sorting-Algorithm-Performance-Comparison.git
   cd sorting-algorithms-comparison

2. **Build and Start the Containers**

   To build and run the containers for the application, run the following command:

   ```bash
   docker-compose up --build

3. **Access pgAdmin4**

- Open a browser and navigate to [http://localhost:5050](http://localhost:5050).
- Login with the credentials provided in the `docker-compose.yml` file.

### Check Database

Once logged into pgAdmin4, connect to the `sorting_db` and inspect the `sorting_results` table to view benchmark results.

## Running the Application

The application automatically runs `main.py` when the Docker container starts. The script generates a random array, benchmarks various sorting algorithms, and stores the results in the PostgreSQL database.

### Manually Run the Application

If you want to run the application manually inside the container, use the following command:

  
    docker exec -it sorting_app python main.py

## Database Schema

The PostgreSQL database contains the following schema for storing benchmark results:

    
    CREATE TABLE sorting_results
    (
    id SERIAL PRIMARY KEY,
    algorithm_name VARCHAR(50),
    array_size INTEGER,
    execution_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );


- **id**: A unique identifier for each entry.
- **algorithm_name**: The name of the sorting algorithm used (e.g., "Bubble Sort").
- **array_size**: The size of the array sorted.
- **execution_time**: The time taken to sort the array.
- **created_at**: Timestamp when the result was recorded.

## Future Improvements

- Add more sorting algorithms (e.g., Tim Sort, Shell Sort).
- Integrate with **Power BI** or other visualization tools to provide real-time or graphical insights into sorting performance.
- Implement **multi-threading** to speed up performance in the benchmarking process.
- Support additional database options (e.g., MySQL, SQLite) for storing results.

