import sys
from tqdm import tqdm

def main():
    data = sys.stdin.read()
    data = data.split("\n\n")
    ct = 0
    for block in tqdm(data):
        matrix = []
        for line in block.split("\n"):
            matrix.append(line)
        row = check_symmetry(matrix, 1)
        if row >= 0:
            ct += 100*(row+1)
            continue
        col = check_symmetry(transpose(matrix), 1)
        if col >= 0:
            ct += col+1
    print(ct)

def count_row_diff(matrix, row1, row2):
    n, m = len(matrix), len(matrix[0])
    ct = 0
    for i in range(m):
        if matrix[row1][i] != matrix[row2][i]:
            ct+=1
    return ct

def check_symmetry(matrix, tolerance):
    n = len(matrix)
    for i in range(n-1):
        mismatch = 0
        for j in range(n):
            idx = i+1+i-j
            if 0 <= idx < n:
                mismatch += count_row_diff(matrix, j, idx)
        if mismatch//2 == tolerance: # double ct
            return i
    return -1

def transpose(matrix):
    return ["".join(x) for x in zip(*matrix)]

main()
