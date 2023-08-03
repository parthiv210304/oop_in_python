def decorator(fx):
    def wrapper():
        print("welcome")
        fx()
        print("thanks for using")

    return wrapper
@decorator
def func():
    print("hello")
func()