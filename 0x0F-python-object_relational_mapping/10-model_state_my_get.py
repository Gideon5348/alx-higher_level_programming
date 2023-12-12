#!/usr/bin/python3
"""
Prints the State object with the name from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    session = Session(engine)

    # Query State object with the provided state name
    state_name = sys.argv[4]
    result = session.query(State.id).filter(State.name == state_name).first()

    # Display the result or "Not found" if no match
    print(result[0] if result else "Not found")

    # Close the session
    session.close()
