# ownable.py
class Ownable:
    def __init__(self, owner):
        self.owner = owner

    def is_owner(self, user):
        return user == self.owner

    def require_owner(self, user):
        if not self.is_owner(user):
            raise PermissionError("User does not have the necessary privileges.")
    
    def set_owner(self, owner):
        self.owner = owner
