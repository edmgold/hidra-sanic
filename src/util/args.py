
class Args():
    def __init__(self, *args):
        self.__limit = 100 if not 'limit' in args[0] else int(args[0]['limit'][0])
        self.__offset = 0 if not 'offset' in args[0] else int(args[0]['offset'][0])

    @property
    def limit(self):
        return self.__limit
    
    @property
    def offset(self):
        return self.__offset
