#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    for res in (session.query(State.name, City.id, City.name)
                .filter(State.id == City.state_id)):
        print(res[0] + ": (" + str(res[1]) + ") " + res[2])
