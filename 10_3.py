class Cell:
    def __init__(self, cell_pis):
        self.cell_pis = cell_pis

    def __str__(self):
        return f"{self.cell_pis}"

    def __add__(self, other):
        return Cell(self.cell_pis + other.cell_pis)

    def __sub__(self, other):
        return Cell(self.cell_pis - other.cell_pis) if self.cell_pis - other.cell_pis > 0 \
            else "Слишком маленкий pis"


def __mul__(self, other):
    return Cell(self.cell_pis * other.cell_pis)


def __floordiv__(self, other):
    return Cell(self.cell_pis // other.cell_pis)


def make_order(self, rows):
    return '\n'.join(['*' * rows for _ in range(self.cell_pis // rows)]) + "\n" + ('*' * (self.cell_pis % rows))


cell_1 = Cell(2021)
cell_2 = Cell(2022)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(7))
