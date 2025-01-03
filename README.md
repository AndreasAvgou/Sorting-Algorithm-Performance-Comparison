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

