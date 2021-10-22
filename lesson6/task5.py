class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} pen started drawing a line')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} pencil has started to draw a thin line')

class Handle(Stationery):
    def draw(self):
        print(f'Handle {self.title} is starting to draw a bold line')



s1 = Pen('My Best Pen')
s1.draw()

s2 = Pencil('Gray Pencil')
s2.draw()

s3 = Handle('Red Marker')
s3.draw()
