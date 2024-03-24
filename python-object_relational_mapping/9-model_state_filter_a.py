#!/usr/bin/python3
"""
Lists all State objects that contain the letter `a`
from the database `hbtn_0e_6_usa`
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
    try:
        for instance in session.query(State).filter(State.name.contains("a")):
            print(instance.id, instance.name, sep=": ")
    except Exception as e:
        print(e.args[0])
