from flask import Flask
from flask_restful import Api
from resources.user import UserResource
from resources.student import StudentResource, StudentListResource
from resources.classes import ClassResource, ClassListResource
from resources.result import ResultResource, ResultListResource
from flask_jwt import JWT
from security import authenticate, identity

app=Flask(__name__)
api=Api(app)
app.secret_key="akshay"
jwt=JWT(app, authenticate, identity)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserResource,'/register')
api.add_resource(StudentResource,'/student/prn/<int:prn>')
api.add_resource(ClassResource,'/class/<string:classname>')
api.add_resource(ResultResource,'/result/prn/<int:prn>')
api.add_resource(StudentListResource,'/students')
api.add_resource(ClassListResource,'/classes')
api.add_resource(ResultListResource,'/results')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=1111, debug=True)