import pytest
from lib.greeting import greeting

class Test_Greeting2:
    def test_greet2(self):
        greet = greeting('chris')
        assert greet == 'Hello chris'