class User():
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self,name):
        self._name = name
    def attack(self):
        User.attack(self) #we can do this for not repeat ourselves
        print('asdasd')

class Archer(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())