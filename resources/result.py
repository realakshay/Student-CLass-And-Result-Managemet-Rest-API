from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.result import ResultModel

class ResultResource(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("prn", type=int, required=True, help="Cannot be blank")
    parser.add_argument("cgpa", type=float, required=True, help="Cannot be blank")

    def get(self, prn):
        result=ResultModel.find_by_prn(prn)
        if result:
            return result.json()
        return {"message":"not found"}
    
    def post(self, prn):
        data=ResultResource.parser.parse_args()
        result=ResultModel.find_by_prn(prn)
        if result:
            return {"message":"Already Exist"}
        result=ResultModel(data['prn'],data['cgpa'])
        result.insert_in_db()
        return {"message":"Insert Success"}
    
    def put(self,prn):
        data=ResultResource.parser.parse_args()
        result=ResultModel.find_by_prn(prn)
        if result:
            result.cgpa=data['cgpa']
            result.insert_in_db()
            return result.json()
        return {"message":"does not foun to update"}
    
    @jwt_required
    def delete(self,prn):
        result=ResultModel.find_by_prn(prn)
        if result:
            result.delete_from_db()
            return {"message":"Delete success"}
        return {"message":"Not found for delete"}
    
class ResultListResource(Resource):

    def get(self):
        return {"Result":[x.show() for x in ResultModel.query.all()]}

class ResultListWithStudentDetails(Resource):
    def get(self):
        return {"Result":[x.json() for x in ResultModel.query.all()]}

