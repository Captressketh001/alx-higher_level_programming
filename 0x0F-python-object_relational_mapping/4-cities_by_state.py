#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states WHERE states.id=cities.state_id\
                ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()

