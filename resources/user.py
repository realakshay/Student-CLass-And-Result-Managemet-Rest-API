from flask_restful import Resource, reqparse
from models.user import UserModel

class UserResource(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True,help="Cannot be blank")
    parser.add_argument("password",type=str,required=True,help="Cannot be blank")

    def post(self):
        data=UserResource.parser.parse_args()
        user=UserModel.find_by_username(data['username'])
        if user:
            return {"message":"Alredy Exist"}
        else:
            user=UserModel(data['username'], data['password'])
            user.insert_in_db()
            return {"message":"User Register Success"}