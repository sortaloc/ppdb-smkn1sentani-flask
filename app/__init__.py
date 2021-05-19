from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'ioafhwa97e9032iakdnwi'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ppdb.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ppdbs.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db  = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Silahkan login <br> untuk mengakses halaman ini'
login_manager.login_message_category = 'danger'

from app import routes