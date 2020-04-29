from flask import Flask
from flask_restful import Api
from resources.user import UserResource

app=Flask(__name__)
api=Api(app)
app.secret_key="akshay"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserResource,'/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=1111, debug=True)