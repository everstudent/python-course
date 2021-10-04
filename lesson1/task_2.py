input = int(input('Please input any amount of seconds: '))

hours = input // 3600
minutes = (input - hours * 3600) // 60
seconds = input - hours*3600 - minutes * 60

print('%02d:%02d:%02d' % (hours, minutes, seconds))
