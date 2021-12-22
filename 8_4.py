from functools import wraps


def val_checker(ch=0):
    def _checker(cal_cube):

        @wraps(cal_cube)
        def chek(x):
            if ch(x) == 1:
                m = 'Меньше нуля'
                raise ValueError(m)
            else:
                return cal_cube(x)

        return chek

    return _checker


@val_checker(lambda x: x < 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)