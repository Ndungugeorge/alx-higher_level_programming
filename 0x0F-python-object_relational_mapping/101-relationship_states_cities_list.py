#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    for res in session.query(State).order_by(State.id):
        print(res.id, res.name, sep=": ")
        for city_ins in res.cities:
            print(" " * 4, end="")
            print(city_ins.id, city_ins.name, sep=": ")
