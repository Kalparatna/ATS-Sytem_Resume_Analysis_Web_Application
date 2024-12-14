import mysql.connector

# Replace these values with your actual MySQL connection details
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',  # or your MySQL host IP
    'database': 'db',
    'raise_on_warnings': True
}

try:
    # Establish the database connection
    db = mysql.connector.connect(**config)
    print("Connected to MySQL!")

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SELECT query for the 'resume_text' column
    cursor.execute("SELECT resume_text FROM applicant_data;")

    # Fetch all rows from the result set
    data = cursor.fetchall()

    # Close cursor and database connection
    cursor.close()
    db.close()

    # Print the fetched 'resume_text' data
    for row in data:
        print(row[0])  # Assuming there's only one column in the result (resume_text)

except mysql.connector.Error as err:
    print(f"Error: {err}")
