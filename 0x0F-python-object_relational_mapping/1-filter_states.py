#!/usr/bin/python3
"""
Lists all states with a name starting with N from "hbtn_0e_0_usa"
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    sql_query = """
    SELECT *
    FROM states
    WHERE name COLLATE Latin1_General_CS LIKE 'N%'
    ORDER BY id;
"""
    cur.execute(sql_query)

    states = cur.fetchall()

    for state in states:
        print(state)
