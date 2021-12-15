# 6_1
# file_parssing_logs = open('nginx_logs.txt', 'r', encoding='utf-8')
# result = ((one_line.split()[0], one_line.split()[5][1:], one_line.split()[6]) for one_line in file_parssing_logs)
# result_logs = [val for val in result]
# print(result_logs)
# file_parssing_logs.close()

# 6_2 поск спамера
my_dict = {}
count = 1
res = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as lines:
    for line in lines:
        line = line.split(',')
        line = line[0].replace('(', '')
        if line in my_dict.keys():
            my_dict[line] += 1
        else:
            count = 1
            my_dict[line] = count
for k, v in my_dict.items():
    if v > count:
        count = v
        res.clear()
        res[count] = k

print('IP спамера:', res[count])
