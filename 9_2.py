class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asph_mass(self):
        sum_mass = self._length * self._width * 25 * 5
        return sum_mass // 1000


a = Road(5000, 20)
print(f'{a.asph_mass()}т.')
