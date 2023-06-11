class Member:
    def __init__(self, name, date_of_birth, premium, active=True, id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.premium = premium
        self.active = active
        self.id = id