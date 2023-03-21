import sqlite3
from flask import Flask, render_template, request, session

app = Flask (__name__)

def get_db_connection():
    conn = sqlite3.connect('CourseCatalog.db')
    conn.row_factory = sqlite3.Row
    return conn



@app.route('/')
def index():
    conn = get_db_connection()
    lstCourse = conn.execute('''select * from Catalog''').fetchall()
    #code to filter the subject list
    cursor = conn.cursor()
    cursor.execute("SELECT subject FROM catalog")
    rows = cursor.fetchall()
    data = [row[0] for row in rows]
    data = list(set(data))
    conn.close()
    return render_template("index.html", lstCourse=lstCourse, data=data)

@app.route('/favorite-class/<int:class_id>', methods=['POST'])
def favorite_class(class_id):
    if 'favorite_classes' not in session:
        session['favorite_classes'] = []
    session['favorite_classes'].append(class_id)
    return '', 204

@app.route('/favorites')
def favorites():
    conn = get_db_connection()
    favorite_classes = session.get('favorite_classes', [])
    classes = conn.execute ("SELECT name FROM catalog")# retrieve list of classes from database
    favorite_classes = [c for c in classes if c['name'] in favorite_classes]
    return render_template('favorites.html', favorite_classes=favorite_classes)
 
@app.route('/<Classes>')
def Template(Classes):
    conn = get_db_connection()
    lstCourse = conn.execute('''select * from Catalog''').fetchall()
    conn.close()
    return render_template("ClassTemplate.html", lstCourse=lstCourse, classes = Classes)

@app.route('/plan')
def Plan():
    return render_template("planner.html")

@app.route('/grading')
def Grade():
    return render_template("grading.html")

@app.route('/test')
def Test():
    return render_template("testing.html")

@app.route('/blended')
def Blend():
    return render_template("blended.html")



if __name__ == "__main__":
    app.run(debug=True)