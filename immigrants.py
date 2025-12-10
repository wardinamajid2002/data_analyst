
import pandas as pd
import sqlite3

csv_file_path = 'Building_Permits.csv'  # Replace with your actual file path
table_name = 'immigrants'   # Choose a name for your SQL table
database_file = ':memory:'       # Use ':memory:' for temporary, fast operations, or 'my_database.db' to save to disk

# --- Step 1 & 2: Load CSV into Pandas DataFrame ---
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")
    exit()

# --- Step 3 & 4: Create SQLite connection and write DataFrame to SQL table ---
conn = sqlite3.connect(database_file)
# 'if_exists="replace"' drops the table if it already exists and creates a new one
df.to_sql(table_name, conn, if_exists='replace', index=False)

# --- Step 5: Execute SQL Queries ---
# Example 1: Select all data
query_1 = f'SELECT * FROM {table_name} LIMIT 10'


print(f"\n--- Results for: {query_1} ---")

results_all_1 = pd.read_sql_query(query_1, conn)
print(results_all_1)

# Example 2: Run a specific query (e.g., filter and group)
query_2 = f'SELECT "Permit Creation Date" FROM {table_name} '


print(f"\n--- Results for: {query_2} ---")

results_all_2 = pd.read_sql_query(query_2, conn)
print(results_all_2)

#3
query_3 = f'SELECT "Permit Number","Permit Type","Current Status" FROM {table_name} GROUP BY "Current Status" ORDER BY "Permit Creation Date" '


print(f"\n--- Results for: {query_3} ---")

results_all_3 = pd.read_sql_query(query_3, conn)
print(results_all_3)

#4
query_4 = f'SELECT DISTINCT "Permit Type Definition" FROM {table_name} ORDER BY "Permit Type Definition" ASC '


print(f"\n--- Results for: {query_4} ---")

results_all_4 = pd.read_sql_query(query_4, conn)
print(results_all_4)

#5
query_5 = f'SELECT COUNT(*) AS Total_Immigrants FROM {table_name} '


print(f"\n--- Results for: {query_5} ---")

results_all_5 = pd.read_sql_query(query_5, conn)
print(results_all_5)

#6
query_6 = f'SELECT "Zipcode","Current Status" FROM {table_name} WHERE "Permit Number"IN (SELECT "Permit Number" FROM {table_name} ORDER BY "Permit Number" ASC) LIMIT 15'


print(f"\n--- Results for: {query_6} ---")

results_all_6 = pd.read_sql_query(query_6, conn)
print(results_all_6)

#7
# query_7 = f'SELECT MAX("Completed Date") FROM {table_name}'
query_7 = f'SELECT MIN("Completed Date") FROM {table_name}'

print(f"\n--- Results for: {query_7} ---")

results_all_7 = pd.read_sql_query(query_7, conn)
print(results_all_7)


# --- Clean up ---
conn.close()
