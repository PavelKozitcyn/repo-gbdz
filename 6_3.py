from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as name_file:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby_file:
        if len(name_file.readlines()) >= len(hobby_file.readlines()):
            name_file.seek(0)
            hobby_file.seek(0)
            with open('users_name_hobby.csv', 'w', encoding='utf-8') as user_hobby_file:
                name_list = [name.strip() for name in name_file]
                hobby_list = [hobby.strip() for hobby in hobby_file]
                user_hobby_dict = {key: val for key, val in zip_longest(name_list, hobby_list)}
                print(user_hobby_dict, file=user_hobby_file)
        else:
            exit(1)
