from flask_restful import Resource, reqparse
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