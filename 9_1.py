import time
from time import sleep


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        a = 0
        while a < 10:
            for i in self.__color:
                print(i)
                if i == 'красный':
                    time.sleep(7)
                    a += 1
                elif i == 'жёлтый':
                    time.sleep(2)
                    a += 1
                else:
                    time.sleep(5)
                    a += 1


step = TrafficLight()
print(step.running())
