class PlayerCharacter:
    membership = True
    def __init__(self, name):
        if (self.membership):
            self._name = name # we can do _name but still no guaranteed . there is no true privacy
    
    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('asd')
player1._name = '!!!' # we can still modify it as said no guaranteed
