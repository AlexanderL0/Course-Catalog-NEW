from flask import Flask, render_template
##from flask_sqlalchemy import SQLAlchemy




app = Flask (__name__)
##app.secret_key = "jChung"

##app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
##app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

##db = SQLAlchemy(app)


##class Data (db.Model):
##    id = db.Column(db.Integer, primary_key = True)
  ##  name =db.Column(db.String(100))
    ##teacher =db.Column(db.String(100))
    ##subject =db.Column(db.String(100))

    ##def __init__(self, name, teacher, subject):
      ##  self.name = name
        ##self.teacher = teacher
        ##self.subject = subject
        

@app.route('/')
def Index():
    return render_template("index.html")

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