import sys
from collections import deque

deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
move = {"|": [0, 2], '-': [1, 3], 'L': [2, 1], 'J': [2, 3], '7': [0, 3], 'F': [1, 0], "S": [0, 1, 2, 3]}
dmove = {}
for k, v in move.items():
    dmove[k] = [deltas[x] for x in v]

recv = {}

def has_open_north(symbol):
    return symbol in ['|', 'L', 'J']

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    matrix = []
    for line in data:
        matrix.append(list(line))
    
    nodes, max_depth = get_path_nodes(matrix)
    xray_mask = xray(matrix, nodes)
    ct = 0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if xray_mask[i][j] and (i, j) not in nodes:
                ct+=1
    print(max_depth)
    print(ct)
    
            
def print_matrix_z(matrix, path_nodes):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if (i, j) in path_nodes:
                print(val, end='')
            elif val == '.':
                print("0", end='')
            else:
                print(" ", end='')
        print()

def xray(matrix, path_nodes):
    mask = [[False] * len(matrix[0]) for _ in matrix]
    for nx in range(0, len(matrix)):
        count = 0
        for ny in range(0, len(matrix[0])):
            on_path = (nx, ny) in path_nodes
            if on_path and has_open_north(matrix[nx][ny]):
                count += 1
            mask[nx][ny] = count % 2 != 0
    return mask



def get_path_nodes(matrix):
    loc = (-1, -1)
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 'S':
                loc = (i, j)
                break
    visited = [[False] * len(matrix[0]) for _ in matrix]
    visited[loc[0]][loc[1]] = True
    queue = deque([(loc, 0)])
    path_nodes = [loc]
    max_depth = 0
    while queue:
        #print(len(queue))
        loc, depth = queue.popleft()
        i, j = loc
        #print(loc)
        max_depth = max(max_depth, depth)
        dxy = dmove[matrix[i][j]]
        for dx, dy in dxy:
            x, y = i + dx, j + dy
            if visited[x][y]:
                continue
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                continue
            if matrix[x][y] == '.':
                continue
            reciever = matrix[x][y]
            rmove = dmove[reciever]
            if any(zxcv == (-dx, -dy) for zxcv in rmove):
                path_nodes.append((x, y))
                queue.append(((x, y), depth + 1))
                visited[x][y] = True
    return path_nodes, max_depth
        
main()