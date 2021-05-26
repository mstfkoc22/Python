#iterable -> list,dictionary,tuple,set,string
#iterate -> one by one check each item in collection
user = {
    'name': 'Anıl',
    'age': 24
}

for item in user.items():
    print(item)

for key, value in user.items():
    print(key)
    print(value)