def my_func(some_num):
    for n in range(1, some_num + 1, 2):
        yield n


some_gen = my_func(int(input('Введи число:')))
for i in some_gen:
    print(i)
print(next(some_gen))
