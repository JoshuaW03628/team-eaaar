from sqlalchemy import Column, Integer, String
from .. import db

class Data(db.Model):
  __tablename__ = "data"

  id = Column(Integer, primary_key=True)
  col = Column(String(255))

  def __init__(self, col):
    self.col = col

  def to_dict(self):
    return {
      "id": self.id,
      "col": self.col,
    }
  
def init_data():
  if not len(db.session.query(Data).all()) == 0:
    return
  
  data_data = [
    "Hello!",
    "I",
    "Love",
    "EAAAR",
  ]

  data_objects = [Data(data) for data in data_data]
  for data in data_objects:
    try:
      db.session.add(data)
      db.session.commit()
    except Exception as e:
      print("error while creating data table: " + str(e))
      db.session.rollback()
