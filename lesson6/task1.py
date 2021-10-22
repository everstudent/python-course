import time

class TrafficLight:
    __color = 'red'

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            pause = 7
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            pause = 2
            self.__color = 'green'
        else:
            self.__color = 'red'
            pause = 10

        print(f'Switching to {self.__color} and waiting for {pause} seconds...');
        time.sleep(pause)
        print('ok, done')


color = input('Input start color (red, yellow, green): ')
tl = TrafficLight(color)
tl.running()
