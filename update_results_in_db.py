import psycopg2
import os

def update_results_in_db(algorithm_name, array_size, execution_time):
    try:
        conn = psycopg2.connect(
            host="db",
            port="5432",
            user="postgres",
            password="mysecretpassword",
            dbname="sorting_db"
        )
        cur = conn.cursor()

        query = """
        INSERT INTO sorting_results (algorithm_name, array_size, execution_time)
        VALUES (%s, %s, %s);
        """
        
        cur.execute(query, (algorithm_name, array_size, execution_time))
        
        conn.commit()
        print(f"Inserted data for {algorithm_name} with array size {array_size} and execution time {execution_time:.6f}")

    except Exception as e:
        print(f"Error inserting data: {e}")
    
    finally:
        if conn:
            cur.close()
            conn.close()
