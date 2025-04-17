from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
