from team_eaaar import app, db
from team_eaaar.api import api
from flask_cors import CORS
from team_eaaar.model import model

app.register_blueprint(api.data)

@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all() 
        model.init_data()

if __name__ == "__main__":
  cors = CORS(app)
  app.run(debug=True, host="0.0.0.0", port="3749")