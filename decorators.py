##function copy
def welcome():
    return "Welcome to the advanced python course"
welcome()
wel=welcome
wel()
del welcome
print(wel())

def main_welcome(func):
    msg="Welcome"
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func()
        print("please learn these concepts properly")

    return sub_welcome_method()
# main_welcome(print)



@main_welcome
def course_introduction():
    print("This is an advanced python course")


def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello")

say_hello()