# ownable.py
class Ownable:
    def __init__(self, owner):
        self.owner = owner

    def is_owner(self, user):
        return user == self.owner

    def set_owner(self, owner):
        self.owner = owner
