#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    sql = "SELECT cities.name FROM cities JOIN \
                states on cities.state_id = states.id WHERE states.name \
                LIKE BINARY %s ORDER BY cities.id ASC"
    values = (sys.argv[4],)
    cur.execute(sql, values)
    query_rows = cur.fetchall()
    list = [row[0] for row in query_rows]
    print(*list, sep=", ")
    cur.close()
    conn.close()
