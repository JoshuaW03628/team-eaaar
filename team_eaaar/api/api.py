from flask import Blueprint
from flask_restful import Api, Resource
from .. import db
from ..model.model import Data

data = Blueprint("data", __name__)
data_api = Api(data)

class Data_API(Resource):
  def get(self):
    all_data = db.session.query(Data).all()

    print(data)

    if all_data:
      return [data_object.to_dict() for data_object in all_data]
    return "error getting user", 400

data_api.add_resource(Data_API, "/data")