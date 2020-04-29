from flask_restful import Resource, reqparse
from models.student import StudentModel

class StudentResource(Resource):

    parser=reqparse.RequestParser()

    parser.add_argument("prn",type=int,required=True,help="Cannot be blank")
    parser.add_argument("name",type=str,required=True,help="Cannot be blank")
    parser.add_argument("mobile",type=str,required=True,help="Cannot be blank")
    parser.add_argument("email",type=str,required=True,help="Cannot be blank")
    parser.add_argument("department",type=str,required=True,help="Cannot be blank")
    parser.add_argument("classid",type=int,required=True,help="Cannot be blank")

    def get(self,prn):
        student=StudentModel.find_by_prn(prn)
        if student:
            return student.json()
        return {"message":"Not found"}
    
    def post(self,prn):
        data=StudentResource.parser.parse_args()
        student=StudentModel.find_by_prn(prn)
        if student:
            return {"message":"Already Exists"}
        student=StudentModel(data['prn'], data['name'], data['mobile'], data['email'], data['department'], data['classid'])
        student.insert_in_db()
        return {"message":"Insert Success"}