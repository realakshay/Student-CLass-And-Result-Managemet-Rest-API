from flask_restful import Resource, reqparse
from models.classes import ClassModel

class ClassReource(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument("classname", type=str, required=True, help="cannot be blank")
    parser.add_argument("cc", type=str, required=True, help="cannot be blank")

    def get(self,classname):
        classes=ClassModel.find_by_classname(classname)
        if classes:
            return classes.json()
        return {"message":"Not found"}
    
    def post(self,classname):
        data=ClassReource.parser.parse_args()
        classes=ClassModel.find_by_classname(classname)
        if classes:
            return {"message":"This class already exist"}
        classes=ClassModel(data['classname'], data['cc'])
        classes.insert_in_db()
        return {"message":"Insert Success"}
    
    def put(self,classname):
        data=ClassReource.parser.parse_args()
        classes=ClassModel.find_by_classname(classname)
        if classes:
            classes.cc=data['cc']
            classes.insert_in_db()
            return {"message":"update success"}
        return {"message":"not found for update"}