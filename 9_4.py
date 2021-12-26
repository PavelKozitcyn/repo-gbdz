class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Auto{self.name} going')

    def stop(self):
        print(f'Auto{self.name} stoping')

    def turn(self):
        print(f'Auto{self.name} turning')

    def show_speed(self):
        return f'Auto{self.name} It has speed {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'Auto{self.name} It has speed {self.speed}' \
               f'WARNING' if self.speed > 60 else super().show_speed


class WorkCar(Car):
    def show_speed(self):
        return f'Auto{self.name} It has speed {self.speed}' \
               f'WARNING' if self.speed > 40 else super().show_speed


class SportCar(Car):
    """ none"""


class PoliceCar(Car):
    Car.is_police = True


t = TownCar(90, 'red', 'bmw')
w = WorkCar(78, 'logan', 'reno')
s = SportCar(162, 'black', 'VestaSport')
p = PoliceCar(15, 'white-blue', 'uaz')

cars = [t, w, s, p]
for val in cars:
    val.go()
    print(val.color)
    print(val.show_speed())
    val.turn()
    val.stop()
