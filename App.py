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

@app.route('/psych')
def Psych():
    return render_template("psych.html")
  
@app.route('/comp')
def Comp():
    return render_template("comp.html")

@app.route('/ClassTemplate')
def Econ():
    return render_template("ClassTemplate.html")

@app.route('/stats')
def Stats():
    return render_template("stats.html")

@app.route('/multi')
def Multi():
    return render_template("multi.html")

@app.route('/bc')
def Bc():
    return render_template("bc.html")

@app.route('/APUSH')
def Apush():
    return render_template("APUSH.html")

@app.route('/chinese4')
def Chinese4():
    return render_template("chinese4.html")

@app.route('/lang')
def Lang():
    return render_template("lang.html")

@app.route('/physicsC')
def PhysicsC():
    return render_template("physicsC.html")





if __name__ == "__main__":
    app.run(debug=True)