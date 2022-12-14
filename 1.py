class Mixin:
    @staticmethod
    def turn_on_radio(value):
        raise NotImplementedError('turn_on_radio() нужно переопределить в дочернем классе')


class Vehicle:
    def __init__(self, position):  # position: кортеж (10, 20)
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")


class Car(Vehicle, Mixin):
    def __init__(self, position):
        super().__init__(position)

    @staticmethod
    def turn_on_radio(value):
        print(f'Playing {value}')


class Airplane(Vehicle, Mixin):
    pass


car = Car((10, 20))
print(car.position)
car.turn_on_radio('Moscow FM')