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




if __name__ == "__main__":
    app.run(debug=True)