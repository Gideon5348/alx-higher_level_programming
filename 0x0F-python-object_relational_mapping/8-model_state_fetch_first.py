#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    session = Session(engine)

    # Query the first State object, order by id
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
