from peewee import *
from src.config.database import Database

from marshmallow_peewee import ModelSchema

db = Database.get_sqlite()

class Users(Model):
    name = CharField()
    cidade = CharField()
    
    class Meta:
        database = db

class Create():
    @staticmethod
    def execute():
        db.create_tables([Users], safe=True)


class UsersSchema(ModelSchema):

    class Meta:
        # model: Bind peewee.Model to the Schema
        model = Users