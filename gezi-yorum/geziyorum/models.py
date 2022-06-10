from dataclasses import dataclass
from geziyorum import db



@dataclass
class User(db.Model):
    __tablename = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    activated = db.Column(db.Boolean, default=True)

    
   

    def __init__(self, id, username, email, password, activated):
       self.id = id
       self.username = username
       self.email = email
       self.password = password
       self.activated = activated
    

    @classmethod
    def get_all_users(cls):
        return cls.query.all()


@dataclass
class Employees(db.Model):
    __tablename__ = "EMPLOYEES"


    EMPLOYEE_ID=db.Column(db.Integer, primary_key = True)
    FIRST_NAME = db.Column(db.String)
    LAST_NAME = db.Column(db.String)
    EMAIL = db.Column(db.String)
    PHONE_NUMBER = db.Column(db.String)
    HIRE_DATE = db.Column(db.String)
    JOB_ID = db.Column(db.String)
    SALARY = db.Column(db.String)
    COMMISSION_PCT = db.Column(db.String)
    MANAGER_ID = db.Column(db.String)
    DEPARTMENT_ID = db.Column(db.String)


    
    def __init__(self, EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT,  MANAGER_ID,  DEPARTMENT_ID):
        self.EMPLOYEE_ID = EMPLOYEE_ID
        self.FIRST_NAME  = FIRST_NAME
        self.LAST_NAME = LAST_NAME
        self.EMAIL = EMAIL
        self.PHONE_NUMBER = PHONE_NUMBER
        self.HIRE_DATE = HIRE_DATE
        self.JOB_ID = JOB_ID
        self.SALARY = SALARY
        self.COMMISSION_PCT = COMMISSION_PCT
        self.MANAGER_ID = MANAGER_ID
        self.DEPARTMENT_ID = DEPARTMENT_ID

    
    @classmethod
    def get_all_employees(cls):
        
        return cls.query.all()
       