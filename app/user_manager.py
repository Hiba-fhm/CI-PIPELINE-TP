class UserManager:

    def __init__(self):
        self.users = []

    def add_user(self, name):
        if name not in self.users:
            self.users.append(name)
            return True
        return False

    def get_users(self):
        return self.users

    def delete_user(self, name):
        if name in self.users:
            self.users.remove(name)
            return True
        return False