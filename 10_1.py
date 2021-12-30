class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return f"{str(self.my_matrix[0]).strip('[]').replace(',', ' ')}\n" \
               f"{str(self.my_matrix[1]).strip('[]').replace(',', ' ')}\n" \
               f"{str(self.my_matrix[2]).strip('[]').replace(',', ' ')}\n"

    def __add__(self, other):
        matrix_sum = [[cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)] for row_1, row_2 in
                      zip(self.my_matrix, other.my_matrix)]
        return Matrix(matrix_sum)

    matrix_1 = Matrix([[22, 0, 41], [13, 31, 13], [31, 12, 21]])
    matrix_2 = Matrix([[22, 0, 41], [13, 31, 13], [31, 12, 21]])
    print(matrix_1)
    print(matrix_1 + matrix_1)
