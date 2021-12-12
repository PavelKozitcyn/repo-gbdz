scr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
number_scr = [el for el in scr if scr.count(el) <= 1]
print(number_scr)
