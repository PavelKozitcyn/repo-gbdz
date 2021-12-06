from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["весёлый", "яркий", "зелёный", "утопический", "мягкий"]


def get_jokes(count, repeat=True):
    """ Функция случайной шутки
    
    :param count: аргумент количесва шуток
    :param repeat: аргумент разрешающий брать слова
    :return: None
    """

    n_joke = []
    if repeat == True:
        n_joke = []
        n_joke.append(choice(nouns))
        n_joke.append(choice(adverbs))
        n_joke.append(choice(adjectives))
        print(*n_joke, end=',')
    else:
        for ind in range(count):
            n_joke = []
            n_joke.append(choice(nouns))
            nouns.remove(n_joke[0])
            n_joke.append(choice(adverbs))
            adverbs.remove(n_joke[1])
            n_joke.append(choice(abs(adjectives)))
            adjectives.remove(n_joke[2])
            print(*n_joke, end=', ')

get_jokes(4)