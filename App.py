import sqlite3
from flask import Flask, render_template

app = Flask (__name__)

def get_db_connection():
    conn = sqlite3.connect('CourseCatalog.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    lstCourse = conn.execute('''select * from Catalog''').fetchall()
    conn.close()
    return render_template("index.html", lstCourse=lstCourse)

@app.route('/class')
def Template():
    return render_template("ClassTemplate.html")

@app.route('/honors')
def Honor():
    return render_template("honors.html")

if __name__ == "__main__":
    app.run(debug=True)