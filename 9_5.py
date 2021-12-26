class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Пишем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Чертим карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


s = Stationery('meka')
p = Pen('parcer')
pl = Pencil('constructor')
h = Handle('permoment')

s.draw()
p.draw()
pl.draw()
h.draw()
