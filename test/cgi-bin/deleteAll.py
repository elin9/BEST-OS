#!/usr/bin/python

import sqlite3

def main():
    print("Content-type: text/html")
    print("")
    print("<html><head><title>Delete Account</title></head><body>")
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    c.execute('delete from users;')
    conn.commit()
    conn.close()
    print("Deleted all users.<br>")
    print('Return to <a href="http://elin9.rochestercs.org/">home</a>.')
    print("</body></html>")

main()