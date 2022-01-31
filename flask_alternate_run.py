from flask import Flask #importing the flask class from flask module
from flask_sqlalchemy import  SQLAlchemy #im[porting the SQLAlchemy clas object

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///hint.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255),unique=True)
    email=db.Column(db.String(255),unique=True)

    def __repr__(self)->str:
         return '<User %r>' % self.name

    @classmethod
    def create_user(cls,name:str,email:str)->"User":
        return cls(name=name,email=email)

@app.route("/create_user/<name>/<email>")
def create_user(name,email):
    user=User.create_user(name=name,email=email)
    return " Your name is %s and your email is %s" % (user.name, user.email)

if __name__=="__main__":
    app.run(debug=True)


