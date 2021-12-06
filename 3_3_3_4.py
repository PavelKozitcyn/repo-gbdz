def thesaurus_adv(*args):
    name_dict = {}
    for n in args:
        name_dict.setdefault(n.split()[1][0], {}).setdefault(n.split()[0][0], []).append(n)
    return name_dict


print((thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Борис Голубко", "Сергей Гладеов",
                     "Михаил Савиков", "Николай Арефьев", "Сергей Терентьев", "Владимир Садовый")))
