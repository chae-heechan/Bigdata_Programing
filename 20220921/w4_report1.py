import numpy as np


def main():
    list = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
    matrix = np.array(list)

    print(matrix[1][2])
    print(matrix[2][4])
    print(matrix[1][1:3])
    print(matrix[1:, 2])
    print(matrix[:2, 3:])


main()
