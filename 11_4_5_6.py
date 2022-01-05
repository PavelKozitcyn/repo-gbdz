class Marketbase:
    def __init__(self, *args):
        self.args = {k: [] for k in args}

    def __str__(self):
        return f'Ассортимент:{self.args}'

    def some_list(self):
        return self.args

    def coming_printers(self):
        if len(self.args['Printers']) > 0:
            return f'Приход принтеров'
        else:
            f'Все принтеры кончились'

    def coming_scanes(self):
        if len(self.args['Scanes']) > 0:
            return f'Приход сканеров'
        else:
            f'Все сканеры кончились'

    def coming_xeroxs(self):
        if len(self.args['Xeroxs']) > 0:
            return f'Приход ксероксов'
        else:
            f'Все ксероксы кончились'


class Officebase:
    def __init__(self, name, types):
        self.name = name
        self.types = types


class Printers(Officebase):
    def __init__(self, name, types="Printers"):
        super().__init__(name, types)


class Scanes(Officebase):
    def __init__(self, name, types='Scanes'):
        super().__init__(name, types)


class Xeroxs(Officebase):
    def __init__(self, name, types='Xeroxs'):
        super().__init__(name, types)


base = Marketbase(Printers, Scanes, Xeroxs)
p_1 = Printers('Mi')
p_2 = Printers('Canon')
p_3 = Printers('Hp')
p_4 = Printers('Apple')
s_1 = Scanes('hp')
base.args[p_1.types].append(p_1.name)
base.args[p_2.types].append(p_2.name)
base.args[p_3.types].append(p_3.name)
base.args[p_4.types].append(p_4.name)
base.args[s_1.types].append(s_1.name)
print(base)
print(base.coming_printers())
print(base.coming_scanes())
print(base.coming_xeroxs())
