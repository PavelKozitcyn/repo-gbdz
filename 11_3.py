class MyError(Exception):
    def __init__(self, inf):
        self.inf = inf


my_list = []


def isdig(x):
    try:
        if x.isdigit():
            my_list.append(x)
        else:
            raise MyError('Дай численных символов')
    except MyError as error:
        print(error)


a = 0
while a != 'q':
    a = input('Вводим числа, stop если список полон: ')
    if a == "stop":
        break
    isdig(a)
print(my_list)
