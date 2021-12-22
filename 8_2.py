from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_values_list = [val for val in (*args, *kwargs.values())]
        user_log = [f"{func.__name__}({val}. {type(val)})" for val in user_values_list]
        print(*user_log, *func(*args, **kwargs), sep=",\n")

    return wrapper


@type_logger
def calc_cube(*x, **y):
    user_values_list = [val for val in (*x, *y.values()) if isinstance(val, int) or isinstance(val, float)]
    return [ind ** 3 for ind in user_values_list]


a = calc_cube(5, 21, 9.9, 30, m=24, n=1)
