class PlayerCharacter:
    membership = True
    def __init__(self, name):
        if (self.membership):
            self.name = name
    
    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('asd')
player1.name = '!!!'
player1.speak = 'Booo' #speak is not a function anymore we overrided it

print(player1.speak)