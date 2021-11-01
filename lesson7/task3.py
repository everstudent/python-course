class Cell:
    def __init__(self, total):
        self.total = total

    def __add__(self, v):
        return Cell(v + self.total);

    def __sub__(self, v):

        if v > self.total:
            return v - self.total
        else:
            raise Exception("Error: Second cell is bigger than first cell")

    def __mul__(self, v):
        return v * self.total

    def __truediv__(self, v):
        return self.total // v.total

    def make_order(self, per_row):
        printed = 0
        row = 0
        while printed < self.total:
            if row >= per_row:
                print('')
                row = 0

            print('*', end='')

            row += 1
            printed += 1



    def __gt__(self, v):
        return v > self.total

    def __str__(self):
        return 'Total is: ' + str(self.total)


c1 = Cell(10)
c2 = Cell(8)
c3 = Cell(12)


print('C1 + C2:', c1 + c2)

try:
    print('C1 - C3', c1 - c3)
except Exception as e:
    print(e)


print('C1 * C2:', c1 * c2)

print('C1 // C2:', c1 / c2)


c1.make_order(3)
print()
