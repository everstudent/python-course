class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        output = ''
        for i, row in enumerate(self.matrix):
            for ii in row:
                output = output + str(ii) + ' '
            output = output + "\n"

        return output.strip()

    def __add__(self, other_matrix):
        result = []

        for i, row in enumerate(self.matrix):
            result.append([])
            for ii, col in enumerate(row):
                result[i].append(col + other_matrix[i][ii])

        return Matrix(result)

    def __getitem__(self, a):
        return self.matrix[a]

m1 = Matrix([[1, 1, 2], [2, 3, 4], [6, 3, 1]])
print('First matrix')
print(m1)


m2 = Matrix([[6, 4, 5], [1, 1, 1], [2, 3, 8]])
print('')
print('Second matrix')
print(m2)

print('')
print('M1 + M2')
print(m1 + m2)
