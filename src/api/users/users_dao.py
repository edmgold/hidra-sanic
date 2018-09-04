from src.api.users.users_model import Users

class UserDao(object):

    def find_all(self, args):
        return Users.select().paginate(args.limit, args.offset).dicts()

    def get_by_id(self, id):
        return Users.select().where(Users.id==id).dicts()
        # return Users.get_by_id(id).select().dicts()

    def save(self, user_obj):
        user = Users(name=user_obj['name'], cidade=user_obj['cidade'])
        res = user.save()

        if res:
            return self.get_by_id(user.id)
        else:
            return {'erro'}

    def update(self, id, user_obj):
        user = self.get_by_id(id)
        user.name = user_obj['name']
        user.save()

    def delete(self, id):
        user = Users.delete().where(Users.id==id)
        res = user.execute()

        if res:
            return {'sucesso'}
        else:
            return {'erro'}

