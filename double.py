def double(func):
    def wrapper():
        func()
        print("Lets try that again!")
        func()
    return wrapper

@double
def say_hello():
    print("Hello world!")
    
say_hello()
