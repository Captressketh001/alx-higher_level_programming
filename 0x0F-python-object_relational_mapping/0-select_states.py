#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connecting to MySQL database
    """
    db = MySQLdb.connect(host="localhost", 
            port=3306,
            user=argv[1], 
            passwd=argv[2], 
            db=argv[3])

    """
    Get a cursor
    """
    cur = db.cursor()
    """
    Execute the queries
    """
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


