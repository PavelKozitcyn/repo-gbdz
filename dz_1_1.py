# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
mult = a * b * c
som_sum = a + b +c
print(f' {som_sum} {mult}')





