#!/usr/bin/python3
"""takes in the name of a state as and argument and lists
all cities of that state"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                ORDER BY cities.id")
    city_list = [city[2] for city in cur.fetchall() if city[4] == argv[4]]
    print(", ".join(city_list))
