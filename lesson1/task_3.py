number = int(input('Input number: '))

double_number = int("{0}{0}".format(number))
tripple_number = int("{0}{0}{0}".format(number))

print('{0} + {1} + {2} = {3}'.format(number, double_number, tripple_number, number + double_number + tripple_number))
