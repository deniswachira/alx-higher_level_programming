#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
(safe from MySQL injection)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    states = cur.fetchall()
    if states:
        for state in states:
            if state[1] == sys.argv[4]:
                print(state)
