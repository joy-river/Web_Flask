import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrap_func():
        print("wtf")
        func()

    return wrap_func


@speed_calc_decorator
def fast_function():
    print(__name__)
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    print(__name__)
    for i in range(100000000):
        i * i
