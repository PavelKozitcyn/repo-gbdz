percent = ["процент", "процента", "процентов"]
for result in range(1, 101):
    if 14 >= result >= 11:
        print(str(result) + percent[2])
    elif result % 10 == 1:
        print(str(result) + percent[0])
    elif 4 >= result % 10 >= 2:
        print(str(result) + percent[1])
    else:
        print(str(result) + percent[2])