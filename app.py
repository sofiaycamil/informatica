from flask import Flask, render_template
import sqlite3   
app= Flask(__name__)
#conecxion a la db
def get_db_connection():
    conn=sqlite3.connect('database.db')
    conn.row_factory=sqlite3.row
    return conn
