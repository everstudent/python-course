from abc import ABC, abstractmethod

class Wear(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def consumption(self):
        pass

    @property
    def my_title(self):
        return 'My title is: ' + self.title

    def __add__(self, b):
        return b + self.consumption()

class Costume(Wear):
    def __init__(self, title, h):
        super().__init__(title)
        self.h = h

    def consumption(self):
        return self.h*2 + 0.3

class Palto(Wear):
    def __init__(self, title, v):
        super().__init__(title)
        self.v = v

    def consumption(self):
        return self.v/6.5 + 0.5


wears = [
    Palto('My palto', 1.8),
    Costume('My consume', 0.5),
    Costume('Some other consume', 0.4)
]


print('Total consumption')

total_consumption = 0
for w in wears:
    print(w.my_title)
    total_consumption = w + total_consumption

print('Total consumption', total_consumption)
