odd_cubed = []
some_sum_a = 0
# some_sum_b = 0
# some_sum = 0
# b = 0

# for i in range(1001):
#   if i % 2 != 0:
#        odd_cubed.append(i ** 3)
# print(odd_cubed)
# for i in odd_cubed:
#   b = i
#  some_sum = 0
# while i != 0:
#    digit = i % 10
#   i = i // 10
#  some_sum += digit
# if some_sum % 7 == 0:
#    some_sum_a += b
# print(some_sum_a)

for i in range(1, 1000):
    if i % 2 != 0:
        odd_cubed.append(i ** 3)
print(odd_cubed)
for index, value in enumerate(odd_cubed):
    digit = 0
    while value > 0:
        digit += value % 10
        value //= 10
    if digit % 7 == 0:
        some_sum_a += odd_cubed[index]
    odd_cubed[index] += 17
print(odd_cubed)
print(some_sum_a)

some_sum_a = 0
for index, value in enumerate(odd_cubed):
    digit = 0
    while value > 0:
        digit += value % 10
        value //= 10
    if digit % 7 == 0:
        some_sum_a += odd_cubed[index]
print(some_sum_a)
