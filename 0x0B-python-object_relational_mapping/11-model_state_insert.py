#!/usr/bin/python3
"""adds the state object 'Lousiana'"""
from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
