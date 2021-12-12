some_gen=(num for num in range(1, int(input('Введи число:'))+1, 2))
print(*some_gen)
print(next(some_gen))