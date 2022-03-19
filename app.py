from flask import Flask
from flask.sessions import SecureCookieSessionInterface
from routes import candidate_blueprint
from flask_migrate import Migrate
from flask_login import LoginManager
import models
from models import init_app
#from routes import UPLOAD_FOLDER

app = Flask(__name__)
app.config['SECRET_KEY'] = '7d-dqXDdJUY7tg2HggY2Lw'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///./database/candidaturas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


models.init_app(app)

app.register_blueprint(candidate_blueprint)
login_manager = LoginManager(app)
migrate = Migrate(app, models.db)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

    