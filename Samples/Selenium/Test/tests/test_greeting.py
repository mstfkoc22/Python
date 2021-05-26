import pytest
from lib.greeting import greeting

class Test_Greeting:
    def test_greet(self):
        greet = greeting('chris')
        assert greet == 'Hello chris'

#python -m pytest tests/test_greeting.py
#python -m pytest -v -s