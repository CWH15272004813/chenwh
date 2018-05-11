import os
USERNAME = 'root'
PASSWORD = '616263'
HOST = '127.0.0.1'
RORT = '3306'
DATABASE = 'GRBK'

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOST,RORT,DATABASE)

