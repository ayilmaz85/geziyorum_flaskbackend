from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import oracledb
from sqlalchemy.engine import create_engine


db = SQLAlchemy()


def createApp():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "oracle://hr:1@ORCL"

    DIALECT = 'oracle'
    SQL_DRIVER = 'cx_oracle'
    USERNAME = 'HR'  # enter your username
    PASSWORD = "1"  # enter your password
    HOST = 'localhost'  # enter the oracle db host url
    PORT = "1521"  # enter the oracle port number
    SERVICE = 'orcl'  # enter the oracle db service name
  #  ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + \
   #     PASSWORD + '@' + HOST + ':' + PORT + '/?service_name=' + SERVICE

   # engine = create_engine(ENGINE_PATH_WIN_AUTH)

    connection = oracledb.connect(
        sid="orcl", host="localhost", port=1521, user="hr", password='1')

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    db.init_app(app)

    return app
