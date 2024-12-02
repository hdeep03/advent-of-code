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
        tmatrix = transpose(matrix)
        flag = False
        for i in range(1, len(matrix)):
            if check_horizontal_symmetry(matrix, i):
                ct += i*100
                flag = True
                break
        if flag:
            continue
        for i in range(1, len(tmatrix)):
            if check_horizontal_symmetry(tmatrix, i):
                ct += i
                break
    print(ct)

def transpose(matrix):
    return ["".join(x) for x in zip(*matrix)]

def check_horizontal_symmetry(matrix, row):
    lp = row-1
    rp = row
    if lp < 0:
        return False
    while lp >= 0 and rp <= len(matrix) - 1:
        if matrix[rp] != matrix[lp]:
            return False
        lp -= 1
        rp += 1
    
    return True

main()