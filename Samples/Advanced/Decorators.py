def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('hellloooo')

hello()

def my_decorator2(func):
    def wrap_func(*args,**kwargs):
        func(*args,**kwargs)
    return wrap_func

@my_decorator2
def hello2(greeting, emoji = ':('):
    print(greeting,emoji)

hello('hiiii')