class User():
    def __init__(self,email):
        self._email = email

class Wizard(User):
    def __init__(self,name,email):
        super().__init__(email)
        self._name = name

class Archer(User):
    pass

wizard1 = Wizard('Ali','Ali@ali.com')
print(wizard1._email)