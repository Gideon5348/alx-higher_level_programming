#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Database connection parameters
    username, password, database = argv[1], argv[2], argv[3]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()