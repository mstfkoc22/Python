def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(100)
print(next(g))
print(next(g))

#for item in generator_function(1000):
#    print(item)
#efficent in memory then for i in range(0,30):