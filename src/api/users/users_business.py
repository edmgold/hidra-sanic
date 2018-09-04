from src.api.users.users_dao import UserDao

class UsersBusiness(object):
    def __init__(self):
        self.user_dao = UserDao()
    
    def find_all(self, args):
        return self.user_dao.find_all(args)
    
    def get_by_id(self, id):
        return self.user_dao.get_by_id(id)
    
    def save(self, user):
        return self.user_dao.save(user)       
    
    def delete(self, id):
        return self.user_dao.delete(id)
