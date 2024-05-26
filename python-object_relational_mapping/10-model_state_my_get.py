#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from database `hbtn_0e_6_usa`
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost:3306/{}"""
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == argv[4]).first()
    try:
        print(instance.id)
    except Exception:
        print("Not found")
