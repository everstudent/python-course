class DateClass:
    def __init__(self, date_string):
        if DateClass.is_valid(date_string):
            self.day, self.month, self.year = self.to_num(date_string)
        else:
            raise Exception('Bad date string passed')

    @classmethod
    def to_num(cls, date_string = None):
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def is_valid(date_string):
        list = DateClass.to_num(date_string)
        if len(list) != 3:
            return False

        day, month, year = list
        valid = True

        if day > 31 or day <= 0:
            valid = False

        if month > 12 or month <= 0:
            valid = False

        if year <= 0:
            valid = False

        return valid


# Testing validation
print('Test1:', DateClass.is_valid('11-11-2021'))
print('Test2:', DateClass.is_valid('49-11-2021'))
print('Test3:', DateClass.is_valid('11-14-2021'))
print('Test4:', DateClass.is_valid('11-11'))


# Testing instance creation
d1 = DateClass('01-01-2022')
print('Numeric test:', [type(x) for x in d1.to_num('01-11-2022')])

try:
    d2 = DateClass('41-01-2022')
except Exception as e:
    print('Exception test:', e)
