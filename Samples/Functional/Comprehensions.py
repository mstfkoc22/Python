my_list = [char for char in 'hello']
print(my_list)
my_list2 = [num**2 for num in range(0,100)]
print(my_list2)
my_list3 = [num**2 for num in range(0,100) if num %2 == 0]
print(my_list3)

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items()}
my_dict2 = {num: num*2 for num in [1,2,3]}

print(my_dict)