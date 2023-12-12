#!/usr/bin/python3
"""
Start link class to table in the database.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents the 'states' table in the database.

    Attributes:
        id (int): Auto-incremented unique identifier.
        name (str): String with a maximum of 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the 'states' table in the database
    Base.metadata.create_all(engine)
