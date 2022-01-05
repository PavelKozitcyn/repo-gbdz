class Data:
    def init(self, data):
        self.data = data

    @classmethod
    def mod(tp, dt):
        d, m, y = map(int, dt.split('-'))
        tp.validation(d, m, y)
        return tp.validation(d, m, y)

    @staticmethod
    def validation(d, m, y):

        if d < 31 and m < 12 and m < 2004:
            return f'День {d} Месяц {m} Год {y}'
        else:
            return 'Error'


data_1 = Data.mod('11-3-1994')
print(data_1)
data_2 = Data.mod('9-32-2007')
print(data_2)
