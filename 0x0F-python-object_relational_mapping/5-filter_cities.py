#!/usr/bin/python3
"""List all cities of a given state from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username, password, database, state_name = sys.argv[1:]

    try:
        # Connect to MySQL server running on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute the SQL query to select cities of the given state
        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))

        # Fetch the result and display the results
        rows = cursor.fetchall()
        cities = ', '.join(row[0] for row in rows)
        print(cities)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()
