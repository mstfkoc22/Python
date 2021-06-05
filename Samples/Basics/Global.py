total=0

def count():
    global total
    total += 1
    return total

print(count())


#dependency injection is better
def count(total):
    total+=1
    return total