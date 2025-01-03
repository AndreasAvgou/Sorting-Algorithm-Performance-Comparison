DROP TABLE IF EXISTS sorting_results;

CREATE TABLE sorting_results (
    id SERIAL PRIMARY KEY,
    algorithm_name VARCHAR(50),
    array_size INT,
    execution_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
