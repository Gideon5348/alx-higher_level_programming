#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
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

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session and commit to the database
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

    # Close the session
    session.close()
