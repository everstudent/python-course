class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print(f'Car {self.name} started movement')

    def stop(self):
        print(f'Car {self.name} stopped movement')

    def turn(self, direction):
        print(f'Car {self.name} turned {direction}')

    def show_speed(self):
        print(f'Car {self.name} speed is {self.speed}')

    def is_this_a_police(self):
        print(f'Car {self.name}', 'is a' if self.is_police else 'is not a' , 'police car')


# Town
class TownCar(Car):
    def show_speed(self):
        print(f'Car {self.name} speed is {self.speed}')

        if self.speed > 60:
            print(' --- ! CAR IS TOO FAST FOR TOWN ! --- ')

car1 = TownCar()

car1.speed = 65
car1.color = 'black'
car1.name = 'Renault'

car1.go()
car1.turn('right')
car1.stop()
car1.show_speed()


# Sport
class SportCar(Car):
    pass

car2 = SportCar()
car2.speed = 120
car2.color = 'red'
car2.name = 'Nissan GTR'
car2.show_speed()


# Work
class WorkCar(Car):
    def show_speed(self):
        print(f'Car {self.name} speed is {self.speed}')
        if self.speed > 40:
            print(' --- ! CAR IS TOO FAST FOR WORK ! --- ')

car3 = WorkCar()
car3.speed = 50
car3.color = 'green'
car3.name = 'Volga'
car3.show_speed()
car3.is_this_a_police()


# Police
class PoliceCar(Car):
    is_police = True

car4 = PoliceCar()

car4.speed = 160
car4.color = 'blue'
car4.name = 'Toyota'

car4.show_speed()
car4.is_this_a_police();
