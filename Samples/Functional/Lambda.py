#lambda expressions 1 time anonymous functions which can use for functions we dont need to use it again

my_list = [1,2,3]
print(list(map(lambda item: item*2, my_list)))

a = [(0,2),(4,3),(10,-1),(9,9)]
a.sort(key = lambda x: x[1])
print(a)