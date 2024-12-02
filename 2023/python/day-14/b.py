import sys
from tqdm import tqdm

MAX = 1000000000

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    matrix = []
    for line in data:
        matrix.append(list(line))
    #print_matrix(matrix)
    seen_hm = {}
    first, second = -1, -1
    hsh = hash_matrix(matrix)
    seen_hm[hsh] = 0
    for i in tqdm(range(1, MAX+1)):
        do_cycle(matrix)
        hsh = hash_matrix(matrix)
        if hsh in seen_hm:
            first = seen_hm[hsh]
            second = i
            break
        seen_hm[hsh] = i

    diff = second - first
    print(first, second, diff)
    delta = (MAX - first) % diff
    for i in range(delta):
        do_cycle(matrix)
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

def hash_matrix(matrix):
    s = ''
    for line in matrix:
        s += ''.join(line)
    return s

def do_cycle(matrix):
    for _ in range(len(matrix)):
        shift_north(matrix)
    for _ in range(len(matrix)):
        shift_west(matrix)
    for _ in range(len(matrix)):
        shift_south(matrix)
    for _ in range(len(matrix)):
        shift_east(matrix)


def shift_east(matrix):
    for j in range(len(matrix[0])-1):
        for i in range(len(matrix)):
            if matrix[i][j] == 'O' and matrix[i][j+1] == '.':
                matrix[i][j] = '.'
                matrix[i][j+1] = 'O'
    return matrix

def shift_west(matrix):
    for j in range(len(matrix[0])-1, 0, -1):
        for i in range(len(matrix)):
            if matrix[i][j] == 'O' and matrix[i][j-1] == '.':
                matrix[i][j] = '.'
                matrix[i][j-1] = 'O'
    return matrix

def shift_north(matrix):
    for i in range(len(matrix)-1, 0, -1):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O' and matrix[i-1][j] == '.':
                matrix[i][j] = '.'
                matrix[i-1][j] = 'O'
    return matrix

def shift_south(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'O' and matrix[i+1][j] == '.':
                matrix[i][j] = '.'
                matrix[i+1][j] = 'O'
    return matrix


main()