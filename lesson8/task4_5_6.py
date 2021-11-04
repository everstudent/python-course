from abc import ABC, abstractmethod



# Warehouse class

class WareHouse:
    def __init__(self, title):
        self.title = title
        self.storage = []

    def store(self, tech, quantity, section):
        self.storage.append({
            'tech': tech,
            'quantity': quantity,
            'section': section
        })

    def __str__(self):
        sections = set([t['section'] for t in self.storage])

        output = ''
        for section in sections:
            output += f' === {section} === ' + '\n'

            for t in self.storage:
                if t['section'] == section:
                    output += f" *   {t['quantity']}: {t['tech']}" + '\n'

            output += '\n'

        return output

# Tech classes

class AbstractTech(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Pen(AbstractTech):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def check():
        if len(self.color) >= 3:
            return True

    def __str__(self):
        return f'{self.title}, {self.color} color'


class Scanner(AbstractTech):
    def __init__(self, title, speed):
        super().__init__(title)
        self.speed = speed

    def check():
        if speed >= 10:
            return True

    def __str__(self):
        return f'{self.title}, {self.speed} papers per minute'


class Monitor(AbstractTech):
    def __init__(self, title, pixels):
        super().__init__(title)
        self.pixels = pixels

    def check():
        if self.pixels.isnumeric():
            return True

    def __str__(self):
        return f'{self.title}, {self.pixels} pixels vertical'



# Instanciate techs

tech_list = [
    Pen('Simple Pen', 'Blue'),
    Pen('Gel Pen', 'Red'),
    Scanner('Jet', 50),
    Scanner('Fujitsu', 150),
    Monitor('Samsung', 1920),
    Monitor('LG', 1080)
]



# Store everything in warehouse
w = WareHouse('General werehouse')

for t in tech_list:
    s = input(f'Input {t} section name: ')

    while True:
        try:
            q = int(input(f'Input {t} quantity: '))

            if q <= 0:
                raise Exception('Lower than zero');

            w.store(t, q, s)

            break
        except Exception as e:
            print(f'Wrong quantity, try again (error details: {e})')

print('')
print('Warehouse storage overview:')
print(w)


# Sample output
#
# Warehouse storage overview:
# === office ===
# *   10: Jet, 50 papers per minute
# *   20: Fujitsu, 150 papers per minute
# *   30: Samsung, 1920 pixels vertical
# *   40: LG, 1080 pixels vertical
#
# === pens ===
# *   50: Simple Pen, Blue color
# *   25: Gel Pen, Red color
