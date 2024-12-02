import sys
from collections import deque

deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
move = {"|": [0, 2], '-': [1, 3], 'L': [2, 1], 'J': [2, 3], '7': [0, 3], 'F': [1, 0], "S": [0, 1, 2, 3]}
dmove = {k: [deltas[x] for x in v] for k, v in move.items()}

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    matrix = []
    for line in data:
        matrix.append(list(line))

    max_depth = get_path_nodes(matrix)
    print(max_depth)


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
    max_depth = 0
    while queue:
        loc, depth = queue.popleft()
        i, j = loc
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
                queue.append(((x, y), depth + 1))
                visited[x][y] = True
    return max_depth
        
main()