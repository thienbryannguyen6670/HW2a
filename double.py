def double(func):
    def wrapper():
        func()
        print("Let`s try that again!")
        func()
    return wrapper

@double
def say_hello():
    print("Hello world!")
    
say_hello()
