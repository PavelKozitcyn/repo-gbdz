item_num_translate = {
    'zero': 'ноль', 'one': 'один', 'two': 'два',
    'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
    'nine': 'девять', 'ten': 'десять',
}


def num_translate(numerale):
    return item_num_translate.get(numerale)


# def num_translate(numerale):
#     """
#
#     Эта фунция выдает обишку,хотя по логике должна работать
#
#     """
# if numerale.istitel():
#     return str(item_num_translate.get(numerale.lower())).title()
# return item_num_translate.get(numerale)

print(num_translate(input('Введи  число на английском')))
