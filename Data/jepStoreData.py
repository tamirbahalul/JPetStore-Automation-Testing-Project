class jepStoreData:
    def __init__(self, username, password, exp, beforeLogin):
        self.username = username
        self.password = password
        self.expected = exp
        self.beforeLogin = beforeLogin

