class Road:
    __length = 0
    __width = 0
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def rachet(self):

        rachet = self.length * self.width * 25 * 5 / 1000
        print('Нужная масса асфальта: ',rachet)

Road = Road(20, 5000)
Road.rachet()

