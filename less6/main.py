from time import sleep


# task1
class TrafficLight:
    __color = 'red'

    def running(self):
        print('current color TrafficLight: ', self.__color)
        sleep(7)
        self.__color = 'yellow'
        print('current color TrafficLight: ', self.__color)
        sleep(2)
        self.__color = 'green'
        print('current color TrafficLight: ', self.__color)
        sleep(10)
        self.__color = 'red'
        print('current color TrafficLight: ', self.__color)


# task2
class Road:
    def __init__(self, len, wid):
        self._length = len
        self._width = wid

    def calcRoad(self, weight=25, depth=5):
        print('Требуемая масса асфальта: ', self._length * self._width * weight * depth)


# task3
class Worker:
    _income = {"wage": 50000, "bonus": 0.7}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["wage"] * self._income["bonus"]


# task4
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.limit_speed = 60

    def to_str(self):
        print(f'Car: {self.name}, color: {self.color}, speed: {self.speed}, is police? {self.is_police},'
              f'limit speed: {self.limit_speed}')

    def go(self):
        print('The car went')

    def stop(self):
        print('The car stopped')

    def turn(self, direction):
        print('The car turned ', direction)

    def show_speed(self):
        print('Current speed: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > self.limit_speed:
            print(f'{self.__class__.__name__} over speed')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > self.limit_speed:
            print(f'{self.__class__.__name__} over speed')


class PoliceCar(Car):
    pass


# task5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Launch drawing')


class Pen(Stationery):
    def draw(self):
        print("Drawing ", self.title)


class Pencil(Stationery):
    def draw(self):
        print("Drawing ", self.title)


class Handle(Stationery):
    def draw(self):
        print("Drawing ", self.title)


if __name__ == '__main__':
    # task1
    light = TrafficLight()
    light.running()

    print('2 ----------------')
    # task2
    r1 = Road(20, 5000)
    r1.calcRoad()
    r2 = Road(10, 2500)
    r2.calcRoad()

    print('3 ----------------')
    # task3
    pos1 = Position("Jon", "Rembo", "director")
    pos2 = Position("Vin", "Dizel", "analytic")
    print(f'pos1: {pos1.name} {pos1.surname} {pos1.position}, full_name = {pos1.get_full_name()}, income {pos1.get_total_income()}')
    print(f'pos2: {pos2.name} {pos2.surname} {pos2.position}, full_name = {pos2.get_full_name()}, income {pos2.get_total_income()}')

    print('4 ----------------')
    # task4
    tc = TownCar(70, "red", "Town")
    tc.to_str()
    tc.go()
    tc.show_speed()
    sc = SportCar(100, "black", "Sport")
    sc.limit_speed = 120
    sc.to_str()
    sc.go()
    sc.show_speed()
    sc.turn("right")
    wc = WorkCar(60, "white", "Work")
    wc.limit_speed = 40
    wc.to_str()
    wc.go()
    wc.show_speed()
    pc = PoliceCar(80, "black-white", "Police", True)
    pc.to_str()
    pc.go()
    pc.show_speed()
    sc.turn("left")

    print('5 ----------------')
    # task5
    pen = Pen('Pen')
    pencil = Pencil('Pencil')
    handle = Handle('Handle')
    pen.draw()
    pencil.draw()
    handle.draw()