#!/usr/bin/python3
"""takes in arguments and displays all values in the states table"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall() if state[1] == argv[4]]
