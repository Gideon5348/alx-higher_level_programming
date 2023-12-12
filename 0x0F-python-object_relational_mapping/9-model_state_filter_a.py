#!/usr/bin/python3
"""
Lists all State objects containing letter 'a' from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Create a session to interact with the database
    session = Session(engine)

    # Query State objects containing the letter 'a', order by id
    filtered_states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # Display the results
    for state in filtered_states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
