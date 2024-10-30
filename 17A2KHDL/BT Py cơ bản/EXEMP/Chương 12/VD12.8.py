#Python program showing a scope of object
def some_func():
    print("Inside some_fune")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:",var)
        some_inner_func()
        print("Try printing var from outer function:",var)
        some_func()