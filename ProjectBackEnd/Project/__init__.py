from flask import Flask
# ----------------- databases ---------------
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate






from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#---------------------- upload a picture --------------
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/images/')


app = Flask(__name__)

app.config['SECRET_KEY']='32i4i3n4cmircidxwdxd'


# ------------databases---------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


bcrypt=Bcrypt(app)
login_manager = LoginManager(app)


#---------------------- upload a picture --------------
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from Project import routes

