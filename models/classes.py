from db import db

class ClassModel(db.Model):

    __tablename__="classes"

    id=db.Column(db.Integer)
    classname=db.Column(db.String(80), unique=True, nullable=False)
    div=db.Column(db.String(10), nullable=False)
    cc=db.Column(db.String(80), nullable=False)

    students=db.relationship('StudentModel', lazy='dynamic')

    def __init__(self, classname, div, cc):
        self.classname=classname
        self.div=div
        self.cc=cc
    
    def json(self):
        return {"classname":self.classname,"division":self.div, "Co-Ordinator":self.cc, "students":[x.json() for x in self.students.all()]}
    
    @classmethod
    def find_by_classname(cls,classname):
        return cls.query.filter_by(classname=classname).first()

    def insert_in_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
