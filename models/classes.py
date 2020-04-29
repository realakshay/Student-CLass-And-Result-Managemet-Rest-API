from db import db

class ClassModel(db.Model):

    __tablename__="classes"

    id=db.Column(db.Integer, primary_key=True)
    classname=db.Column(db.String(80), unique=True, nullable=False)
    cc=db.Column(db.String(80), nullable=False)

    students=db.relationship('StudentModel', lazy='dynamic')

    def __init__(self, classname, cc):
        self.classname=classname
        self.cc=cc
    
    def json(self):
        return {"classname":self.classname, "Co-Ordinator":self.cc, "students":[x.json() for x in self.students.all()]}
    
    @classmethod
    def find_by_classname(cls,classname):
        return cls.query.filter_by(classname=classname).first()

    def insert_in_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
