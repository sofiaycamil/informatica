from flask import Flask, render_template
import sqlite3   
app= Flask(__name__)
#conecxion a la db
def get_db_connection():
    conn=sqlite3.connect('database.db')
    conn.row_factory=sqlite3.row
    return conn
#ruta princial de nuestra app
@app.route('/') 
def index():
    conn=get_db_connection()
    rows=conn.execute('select*from fake')
    conn.close()
    return render_template('index_html',rows=rows)
if __name__=='__name__':
 app.run(debug=True)


  