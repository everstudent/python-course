class NotNumberException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'--- !!! Text "{self.text}" is not a number !!! ---';


list = []

while True:
    print('Input any number or "stop" to finish')
    x = input('Input x: ')

    if x == 'stop':
        break

    try:
        if not x.isnumeric():
            raise NotNumberException(x)
        list.append(int(x))
    except NotNumberException as nne:
        print(nne)


print('Result list:', list)
