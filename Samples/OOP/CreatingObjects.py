class PlayerCharacter:
    #Class Object Attribute - static
    membership = True
    def __init__(self, name):
        self.name = name #attribute
    
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Anıl')

print(player1.name)
print(player1.run())


class PlayerCharacter:
    #Class Object Attribute - static
    membership = True
    def __init__(self, name):
        if (self.membership):
            self.name = name #attribute
    
    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')

#-------------

class PlayerCharacter:
    #Class Object Attribute - static
    membership = True
    def __init__(self, name):
        if (self.membership):
            self.name = name #attribute
    
    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')

    #We can call this like PlayerCharacter().adding_things(2,3) -- without create an instance
    #cls classes itself
    @classmethod
    def adding_things(cls,num1,num2):
        return cls('Teddy',num1 + num2) # we created an instance
    
    @staticmethod
    def adding_things2(num1,num2): # difference from classmethod is we don have access to class
        return num1+num2