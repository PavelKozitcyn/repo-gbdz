from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_klass = (name_number for name_number in zip_longest(tutors, klasses))
print(type(tutors_klass))
print(*tutors_klass)
print(next(tutors_klass))
