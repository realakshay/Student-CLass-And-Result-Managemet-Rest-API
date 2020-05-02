from db import db
from models.classes import ClassModel
from models.result import ResultModel

class StudentModel(db.Model):

    __tablename__="students"

    id=db.Column(db.Integer)
    prn=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    mobile=db.Column(db.String(10), nullable=False)
    email=db.Column(db.String(150), nullable=False)
    department=db.Column(db.String(80), nullable=False)
    
    classid=db.Column(db.Integer, db.ForeignKey('classes.id'))
    resultid=db.Column(db.Integer, db.ForeignKey('results.prn'))

    classes=db.relationship('ClassModel')
    results=db.relationship('ResultModel')

    def __init__(self, prn, name, mobile, email, department, classid):
        self.prn=prn
        self.name=name
        self.mobile=mobile
        self.email=email
        self.department=department
        self.classid=classid
        self.resultid=prn

    def json(self):
        return {"prn":self.prn, "name":self.name, "mobile":self.mobile, "email":self.email, "department":self.department, "classId":self.classid, "resultId":self.resultid}

    def show(self):
        return {"name":self.name,"mobile":self.mobile, "email":self.email, "department":self.department}
    
    @classmethod
    def find_by_prn(cls,prn):
        return cls.query.filter_by(prn=prn).first()
    
    @classmethod
    def find_by_email(cls,email):
        return cls.query.filter_by(email=email).first()
    
    def insert_in_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_department(cls, department):
        return cls.query.filter_by(department=department)

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def get_all(cls):
        shall= db.session.query(StudentModel.prn,StudentModel.name,StudentModel.mobile,StudentModel.email, StudentModel.department,ClassModel.classname,ClassModel.cc,ResultModel.cgpa).join(ClassModel).join(ResultModel).order_by(StudentModel.prn,StudentModel.department).all()
        return shall