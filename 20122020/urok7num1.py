class Matrix:
    def __init__(self, spisok, spisok1):
        self.matr = [spisok, spisok1]
        self.spisok = spisok
        self.spisok1 = spisok1

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrixx]))

    def __add__(self):
        matrixx = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.spisok)):

            for j in range(len(self.spisok1[i])):
                matrixx[i][j] = self.spisok[i][j] + self.spisok1[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrixx]))

my_matrix = Matrix([[1, 2, 3], [6, 5, 4], [7, 8, 9]], [[12, 11, 10], [13, 14, 15], [18, 17, 16]])
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(my_matrix.__add__())