import random
import time
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.radix_sort import radix_sort
from update_results_in_db import update_results_in_db  # Import the DB update function


# Function to generate a random array of 1000 integers
def generate_random_array(size=10000, min_val=1, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(size)]


# Compare sorting algorithms and update results in DB
def compare_algorithms():
    arr = generate_random_array()  # Generate a random array of 1000 elements
    
    algorithms = [
        bubble_sort, selection_sort, insertion_sort,
        merge_sort, quick_sort, heap_sort, radix_sort
    ]

    results = {}

    # Measure execution time for each algorithm and update the DB
    for algo in algorithms:
        start = time.time()
        algo(arr[:])  # Sort a copy of the array to avoid modifying the original
        end = time.time()
        
        execution_time = end - start
        array_size = len(arr)
        results[algo.__name__] = execution_time
        
        # Insert data into the database
        update_results_in_db(algo.__name__, array_size, execution_time)

    # Print results
    print("\nComparison of Sorting Algorithms (Execution Time):")
    for algorithm, time_taken in sorted(results.items(), key=lambda item: item[1]):
        print(f"{algorithm}: {time_taken:.6f} seconds")


if __name__ == "__main__":
    compare_algorithms()
