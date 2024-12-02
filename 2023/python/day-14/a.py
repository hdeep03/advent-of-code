import sys
from tqdm import trange

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    matrix = []
    for line in data:
        matrix.append(list(line))
    print_matrix(matrix)
    for _ in trange(len(matrix)):
        shift_north(matrix)
    print_matrix(matrix)
    print(count_Os(matrix))

def print_matrix(matrix):
    for line in matrix:
        print(''.join(line))

def count_Os(matrix):
    ct = 0
    i = len(matrix)
    for line in matrix:
        line = ''.join(line)
        ct += line.count("O")*i
        i -= 1
    return ct

def shift_north(matrix):
    for i in range(len(matrix)-1, 0, -1):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O' and matrix[i-1][j] == '.':
                matrix[i][j] = '.'
                matrix[i-1][j] = 'O'
    return matrix

main()