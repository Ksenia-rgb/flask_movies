from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Config')

#app.config['SECRET_KEY'] = 'SECRET_KEY'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
#app.config['SQLALCHEMY_BINDS'] = {'movies': 'sqlite:///movies.db'}


db = SQLAlchemy(app)


from . import models, views

db.create_all()
