from flask import Flask , render_template , url_for,  request , redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
db =SQLAlchemy(app)

class Employee (db.Model):
    id =db.Column(db.Integer,primary_key=True)
    FirstName = db.Column(db.String(100),nullable=False)
    Lastname = db.Column(db.String(100),nullable=False)
    Gender = db.Column(db.String(1),nullable=False)
    Age =db.Column(db.Integer,nullable=False)
    Blood_Group = db.Column(db.String(3),nullable=False)
    Address= db.Column(db.String(100),nullable=False)
    Mobile_no=db.Column(db.Integer,nullable=False)
    Email_Id = db.Column(db.String(100),nullable=False)

def __init__ (self , FirstName ,lastName,Gender,Age,Blood_Group,Address,Mobile_no,Email_Id):
    self.FirstName=FirstName
    self.Lastname=Lastname
    self.Gender=Gender
    self.Age=Age
    self.Blood_Group=Blood_Group
    self.Address=Address
    self.Mobile_no=Mobile_no
    self.Email_Id=Email_Id
   
     
@app.route('/', methods=['POST','GET'])
def index():
    if request.method =='POST':
        FirstName=request.form['firstName']
        Lastname=request.form['lastName']
        Gender=request.form['gender']
        Age=request.form['age']
        Blood_Group=request.form['bloodGroup']
        Address=request.form['address']
        Mobile_no=request.form['mobileNo']
        Email_Id=request.form['emailId']
        new_employee = Employee(FirstName=FirstName, Lastname=Lastname, Gender=Gender,Age=Age,Blood_Group=Blood_Group,Address=Address,Mobile_no=Mobile_no,Email_Id=Email_Id)


        try:
            db.session.add(new_employee)
            db.session.commit()
            return redirect('/')    
        except:
            return "Data not added to the DB"
            #return render_template('index.html')

    else:
         list1 = Employee.query.all()
         return render_template("index.html",list1=list1)


@app.route('/delete/<int:id>')
def delete(id):
    task = Employee.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "the task isn not deleted "



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)