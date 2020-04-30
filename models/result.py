from models.student import StudentModel
from models.classes import ClassModel
from db import db

class ResultModel(db.Model):

    __tablename__="results"

    id=db.Column(db.Integer, primary_key=True)
    prn=db.Column(db.Integer, primary_key=True)
    cgpa=db.Column(db.Float, nullable=False)

    students=db.relationship('StudentModel', lazy="dynamic")

    def __init__(self,prn,cgpa):
        self.prn=prn
        self.cgpa=cgpa

    def json(self):
        return {"prn":self.prn, "cgpa":self.cgpa, "student":[x.json() for x in self.students.all()]}
    
    @classmethod
    def find_by_prn(cls,prn):
        #return cls.query.join(StudentModel, cls.prn==StudentModel.prn).join(ClassModel, StudentModel.classid==ClassModel.id).first()
        return cls.query.filter_by(prn=prn).first()
    
    def insert_in_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()