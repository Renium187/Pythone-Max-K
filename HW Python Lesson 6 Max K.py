# Задача № 1
import time

class TrafficLight:
    __trafficlight_colour = None
    def __running(self):
        i = 0
        while i < 3:
            self.__trafficlight_colour = 'Red'
            print(self.__trafficlight_colour)
            time.sleep(7)
            self.__trafficlight_colour = 'Yellow'
            print(self.__trafficlight_colour)
            time.sleep(2)
            self.__trafficlight_colour = 'Green'
            print(self.__trafficlight_colour)
            time.sleep(4)
            i += 1

my_tl = TrafficLight()
my_tl._TrafficLight__running()

# Задача № 2

class Road:
    def __init__(self, my_lenght, my_width):
        self._lenght = my_lenght
        self._width = my_width

    def bitumen_m(self):
        m_result = self._lenght * self._width * 25 * 5
        return m_result

r_road = Road(5000, 10)
print(r_road.bitumen_m())

# Задача № 3

class Worker:
    name = 'Nick'
    surname = 'Nekrasov'
    position = 'Engineer'
    _income = {
        "wage": 50000,
        "bonus": 30000
    }


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        t_inc = self._income["wage"] + self._income["bonus"]
        print(t_inc)

en_pos = Position()
en_pos.get_full_name()
en_pos.get_total_income()

# Задание № 4


class Car:
    speed = 60
    color = 'White and Blue'
    name = 'Ford'
    is_police = True

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости! Ограничение 60 км/ч')
        else:
            print(f'Скорость автомобиля: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости! Ограничение 40 км/ч')
        else:
            print(f'Скорость автомобиля: {self.speed}')


class PoliceCar(Car):
    pass


my_car = Car()
my_car.go()
my_car.stop()
my_car.turn('Право')
my_car.show_speed()
your_car = WorkCar()
your_car.go()
your_car.stop()
your_car.turn('Лево')
your_car.show_speed()

# Задание № 5

class Stationery:
    title = 'Рубенс и Малевич'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}, ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}, карандашем')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}, фломастером')


my_st = Stationery()
my_st.draw()
st_1 = Pen()
st_2 = Pencil()
st_3 = Handle()
st_1.draw()
st_2.draw()
st_3.draw()


Отправляю на проверку