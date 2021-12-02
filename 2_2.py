some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for ind, val in enumerate(some_list):
    if val.isdigit():
        some_list[ind] = f'"{int(val):02}"'
    elif val[1:].isdigit():
        some_list[ind] = f'"{val[0]}{int(val[1:]):02}"'
print(some_list)
print(id(some_list))
print(" ".join(some_list))
print(id(" ".join(some_list)))
