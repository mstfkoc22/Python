from functools import reduce

my_list = [1,2,3]

def find_max(a,b):
    if a > b:
        return a
    return b

print(reduce(find_max,my_list)) 
#Reduce fonksiyonu, döngüye sokabileceğiniz herhangi bir veri tipi içinde,
#veri tipinin içindeki tüm elemanları azaltarak dolaşan ve karşılaştırma yapmaya imkan tanıyan bir yapıdır.