from peewee import MySQLDatabase
from peewee import SqliteDatabase

class Database():
    def get_mysql():
        db = MySQLDatabase('my_app', 
            user='ml_v2', 
            password='ml_v2',
            host='localhost', 
            port=3306)
    
        return db

    def get_sqlite():
        db = SqliteDatabase('teste.db')
    
        return db