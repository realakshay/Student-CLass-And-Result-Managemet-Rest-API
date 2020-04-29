from db import db

class StudentModel(db.Model):

    __tablename__="students"

    prn=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    mobile=db.Column(db.String(10), unique=True, nullable=False)
    email=db.Column(db.String(150), unique=True, nullable=False)
    classid=db.Column(db.Integer, db.ForeignKey('classes.id'))

    classes=db.relationship('ClassModel')

    def __init__(self, prn, name, mobile, email, classid):
        self.prn=prn
        self.name=name
        self.mobile=mobile
        self.email=email
        self.classid=classid

    def json(self):
        return {"prn":self.prn, "name":self.name, "mobile":self.mobile, "email":self.email, "classId":self.classid}
    
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
    def find_all(cls):
        return cls.query.all()