class ComplexNumber:
    def __init__(self, real, unreal):
        self.real = real
        self.unreal = unreal

    def __add__(self, x):
        return ComplexNumber(
            self.real + x.real,
            self.unreal + x.unreal
        )

    def __mul__(self, x):
        return ComplexNumber(
            self.real * x.real - self.unreal*x.unreal,
            self.real * x.unreal + self.unreal*x.real
        )

    def __str__(self):
        if self.unreal < 0:
            return f'{self.real} {"-" if self.unreal == -1 else self.unreal}i';
        else:
            return f'{self.real} +{"" if self.unreal == 1 else self.unreal}i';



# Test multiplication
z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(-1, 1)

print(f'({z1}) * ({z2}) =', z1 * z2)



# Test addition
z1 = ComplexNumber(5, -6)
z2 = ComplexNumber(-3, 2)

print(f'({z1}) + ({z2}) =', z1 + z2)



# Output result:
#
# (2 +3i) * (-1 +i) = -5 -i
# (5 -6i) + (-3 +2i) = 2 -4i
