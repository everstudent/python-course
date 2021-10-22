class Road:
    _length = 0
    _width = 0

    __mass_per_1_sm = 25
    __height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        return self._length * self._width * self.__mass_per_1_sm * self.__height;

r = Road(5000, 20)
print(r.calc_mass(), 'kg')
