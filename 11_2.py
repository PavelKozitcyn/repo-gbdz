class MyError(Exception):
    def __init__(self, inf):
        self.inf = inf


a = int(input('Вводим число больше нуля:'))

try:
    if a == 0:
        raise MyError('На ноль делить нельзя')
except(ValueError, MyError) as error:
    print(error)
else:
    print('Делим 7 на', a)
print(7 / a)
