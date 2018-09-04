from src.api.users.users_business import UsersBusiness
from sanic.response import json
from src.util.apis import Api
from src.util.args import Args

class UsersController(object):
    def __init__(self):
        self.business = UsersBusiness()

    def find_all(self, request):
        args = Args(request.headers)
        user = self.business.find_all(args)

        return json(Api().api_return_pattern(user, args))
    
    def get_by_id(self, request, id):
        return json(self.business.get_by_id(id))
    
    def save(self, request):
        return json(self.business.save(request))

    def delete(self, request, id):
        return json(self.business.delete(id))
