class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина начала движение"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return ("Машина повернула", direction)

    def show_speed(self):
        return 'Текущая скорость',self.name,'равна',self.speed

class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def show_speed(self):
        print('Текущая скорость',self.name,'равна',self.speed)

        if int(self.speed) > 60:
            return 'Скорость',self.name,'превышена'

class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print('Текущая скорость', self.name, 'равна', self.speed)

        if int(self.speed) > 40:
            return 'Скорость', self.name, 'превышена'

class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)



oka = TownCar( 30,'White', 'Oka')
lada = WorkCar( 70,'Rose','Lada', False)

print(oka.show_speed())
print(lada.show_speed())#