#ENVIRONMENT CONFIG
from config import Config

#FLASK IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from flask_rest import routes, models
