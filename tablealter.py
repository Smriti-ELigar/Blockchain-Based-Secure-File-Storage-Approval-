# import sqlite3

# DATABASE = "file_logs.db"  # Replace with your actual database file

# def fetch_all_users():
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()

#     c.execute("ALTER TABLE users ADD COLUMN face_hash TEXT;")
#     conn.commit()
#     conn.close()

#     # Print the results in a readable format
#     print("All Users:")
    

# fetch_all_users()


import sqlite3

DATABASE = "file_logs.db"  # Replace with your actual database file

def show_all_data(table_name):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Fetch all records from the table
    c.execute(f"SELECT * FROM {table_name};")
    records = c.fetchall()

    # Fetch column names
    column_names = [desc[0] for desc in c.description]

    if records:
        print(f"Data from '{table_name}':")
        print(", ".join(column_names))  # Print column headers
        for record in records:
            print(record)
    else:
        print(f"No data found in the table '{table_name}'.")

    conn.close()

# Run the function for a specific table
show_all_data("users")  # Replace "users" with the actual table name if needed


# # import sqlite3

# # conn = sqlite3.connect("file_logs.db")  # Ensure this matches your DATABASE variable
# # c = conn.cursor()

# # # Rename the column from face_hash to face_id
# # c.execute("ALTER TABLE users RENAME COLUMN face_hash TO face_token")

# # conn.commit()
# # conn.close()