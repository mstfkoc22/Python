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
    def __init__(self,arrows):
        self._arrows = arrows

class Hybrid(Wizard,Archer):
    def __init__(self, name,arrows):
        Wizard.__init__(self, name)
        Archer.__init__(self,arrows)

hybrid1 = Hybrid('ali',20)
print(hybrid1.sign_in())
print(hybrid1._name)
print(hybrid1._arrows)