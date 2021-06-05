from collections import Counter,defaultdict,OrderedDict

li = [1,2,3,4,5,6,7,7]

print(Counter(li)) # how many times

dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c']) # returns 5 because c doesnt exist

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['b'] = 2
d['a'] = 1

print(d2 == d) #returns false