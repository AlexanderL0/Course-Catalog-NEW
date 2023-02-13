import sqlite3
from flask import Flask, render_template, request

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

@app.route('/<Classes>')
def Template(Classes):
    conn = get_db_connection()
    lstCourse = conn.execute('''select * from Catalog''').fetchall()
    conn.close()
    return render_template("ClassTemplate.html", lstCourse=lstCourse, classes = Classes)

@app.route('/honors')
def Honor():
    return render_template("honors.html")

@app.route('/penis')
def Chin():
    return render_template("chinese4.html")




if __name__ == "__main__":
    app.run(debug=True)