import time

current_time = time.time()
print(current_time)
def make_bold(func):
    def wrap_bold():
        text = f"<b>{func()}</b>"
        return text

    return wrap_bold

def make_underlined(func):
    def wrap_under():
        text = f"<u>{func()}</u>"
        return text

    return wrap_under

def make_etalic(func):
    def wrap_etalic():
        text = f"<em>{func()}</em>"
        return text
    return wrap_etalic


def speed_calc_decorator(func):
    def wrap_func():
        print("wtf")
        func()

    return wrap_func


# @speed_calc_decorator
# def fast_function():
#     print(__name__)
#     for i in range(10000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     print(__name__)
#     for i in range(100000000):
#         i * i
