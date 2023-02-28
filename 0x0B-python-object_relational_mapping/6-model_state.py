#!/usr/bin/python3
"""link class to table in hbtn_0e_4_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadate.create_all(engine)
