from flask import Flask, jsonify
from flask_restful import Api
from resources.user import UserResource, UserLoginResource, TokenRefresh
from resources.student import StudentResource, StudentListResource
from resources.classes import ClassResource, ClassListResource
from resources.result import ResultResource, ResultListResource, ResultListWithStudentDetails
#from flask_jwt import JWT
from flask_jwt_extended import JWTManager
from security import authenticate, identity
from blacklist import BLACKLIST

app=Flask(__name__)
api=Api(app)
app.secret_key="akshay"
#jwt=JWT(app, authenticate, identity)
jwt=JWTManager(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['JWT_BLACKLIST_ENABLED']=True
app.config['JWT_BLACKLIST_TOKEN_CHECKS']=['access','refresh']

@app.before_first_request           #Create table if not created before request
def create_tables():
    db.create_all()

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity==1:
        return {"is_admin":True}
    return {"is_admin":False}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['identity'] in BLACKLIST


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({'description':"The token has been revoked", 'error':"token_revoked"}),401



api.add_resource(UserResource,'/register')
api.add_resource(UserLoginResource,'/login')
api.add_resource(TokenRefresh,'/refresh')
api.add_resource(StudentResource,'/student/prn/<int:prn>')
api.add_resource(ClassResource,'/class/<string:classname>')
api.add_resource(ResultResource,'/result/prn/<int:prn>')
api.add_resource(StudentListResource,'/students')       #Complete student list with details
api.add_resource(ClassListResource,'/classes')          #Class list without student details
api.add_resource(ResultListResource,'/results')         #Result List without student details
api.add_resource(ResultListWithStudentDetails,'/result/detail')     #Result List with student details


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=1111, debug=True)