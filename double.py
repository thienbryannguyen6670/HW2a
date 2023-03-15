def double(func):
    def wrapper():
        func()
        print("Let's try that again!")
        func()
    return wrapper

@double
def my_function():
    print("Hello, world!")
