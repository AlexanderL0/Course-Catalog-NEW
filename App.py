import sqlite3, json
from flask import Flask, render_template, request, session
#from bs4 import BeautifulSoup

#with open('index.html') as f:
#    soup = BeautifulSoup(f, 'html.parser')

# Find the <script> tag containing the JavaScript list
# script_tag = soup.find('script')

# Get the JavaScript code inside the <script> tag
# js_code = script_tag.string.strip()

# Extract the JavaScript list from the code
# js_list = js_code.split('=')[1].strip().strip(';')

# Convert the JavaScript list to a Python list using the json module
# py_list = json.loads(js_list)

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
   # py_list = json.loads(favoriteClasses)

    return render_template("planner.html",)

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