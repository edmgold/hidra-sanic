from sanic import Blueprint
from src.api.users.users_controller import UsersController
from sanic_openapi import doc
from src.api.users.users_model import Users, UsersSchema
from sanic.response import json

# user_blueprint = Blueprint('users')
user_blueprint = Blueprint('User', '/user')
controller = UsersController()

@user_blueprint.get("/", strict_slashes=True)
@doc.summary("Fetches all Users")
@doc.description("Really gets the job done fetching these users.  I mean, really, wow.")
async def find_all(request):
    print('find_all')

    return controller.find_all(request)

@user_blueprint.get("/<id:int>", strict_slashes=True)
@doc.summary("Get a single user")
@doc.description("Only one")
async def get_by_id(request, id):
    print('get_by_id')

    return controller.get_by_id(request, id)

@user_blueprint.post("/", strict_slashes=True)
@doc.summary("Post a new user")
@doc.description("Post")
@doc.produces(Users)
async def post(request):
    print('post')
    
    return controller.save(request.json)

@user_blueprint.delete("/<id:int>", strict_slashes=True)
@doc.summary("Delete a user")
@doc.description("Delete")
async def delete(request, id):
    print('delete')
    
    return controller.delete(request, id)
