#not global also outside of functions scope
def outer():
    x = "local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()