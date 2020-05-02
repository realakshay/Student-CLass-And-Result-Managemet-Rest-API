from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.student import StudentModel

class StudentResource(Resource):

    parser=reqparse.RequestParser()

    parser.add_argument("prn",type=int,required=True,help="Cannot be blank")
    parser.add_argument("name",type=str,required=True,help="Cannot be blank")
    parser.add_argument("mobile",type=str,required=True,help="Cannot be blank")
    parser.add_argument("email",type=str,required=True,help="Cannot be blank")
    parser.add_argument("department",type=str,required=True,help="Cannot be blank")
    parser.add_argument("classid",type=int,required=True,help="Cannot be blank")

    @jwt_required()
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
    
    def put(self,prn):
        data=StudentResource.parser.parse_args()
        student=StudentModel.find_by_prn(prn)
        if student:
            student.name=data['name']
            student.mobile=data['mobile']
            student.email=data['email']
            student.department=data['department']
            student.classid=data['classid']
            student.insert_in_db()
            return {"message":"Update success"}
        return {"message":"Not found for update"}
    
    @jwt_required()
    def delete(self,prn):
        student=StudentModel.find_by_prn(prn)
        if student:
            student.delete_from_db()
            return {"message":"Delete success"}
        return {"message":"Not found for delete"}

class StudentListResource(Resource):

    def get(self):
        result=StudentModel.get_all()
        students=[]
        for i in result:
            l={"Name":i[0], "Mobile":i[1], "Email":i[2], "Department":i[3], "Class Co.":i[4], "cgpa":i[5]}
            students.append(l)
        return {"Students":students}