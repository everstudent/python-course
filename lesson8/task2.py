class MyZeroException(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f'--- !!! Zero devision error: {self.error} !!! ---';


while True:
    print('=====')
    print('Input x & y or any letter to exit')
    try:
        x = int(input('Input x: '))
        y = int(input('Input y: '))
    except ValueError:
        print('Exiting program, bye...')
        break

    try:
        if y == 0:
            raise MyZeroException(f'I will not divide {x} by zero!')

        print('x/y =', x/y);

    except MyZeroException as de:
        print(de)
