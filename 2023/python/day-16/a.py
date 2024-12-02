import sys
from tqdm import tqdm

deltas_from_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    data = sys.stdin.read()

    matrix = []
    for line in data.splitlines():
        matrix.append(list(line))
    print_matrix(matrix)
    print(get_results(matrix, (0, 0), 1))
    

def get_results(matrix, start, direction):
    visited = [set() for _ in range(4)] # S, E, N, W direction beams, this should mutate
    simulate_beam(start, direction, matrix, visited)
    total_visited = set()
    for _, states in enumerate(visited):
        total_visited = total_visited.union(states)
    return len(total_visited)


def simulate_beam(start, direction, matrix, visited):
    # (0, 1), (1, 0), (0, -1), (-1, 0)
    i, j = start
    while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
        if (i, j) in visited[direction]:
            return  # seems familiar
        
        visited[direction].add((i, j))
        if matrix[i][j] == "." or (direction in [0, 2] and matrix[i][j] == "|") or (direction in [1, 3] and matrix[i][j] == "-"):
            di, dj = deltas_from_direction[direction]
            i += di
            j += dj
            continue
        if matrix[i][j] in ["\\", "/"]:
            (di, dj), direction = handle_collision(direction, matrix[i][j])
            i += di
            j += dj
            continue

        new_directions = list(map(lambda x: x%4, [direction + 1, direction -1]))
        for new_direction in new_directions:
            simulate_beam((i, j), new_direction, matrix, visited)
        return        


def handle_collision(direction, mirror):
    # -> / = 
    if mirror == "/":
        match direction:
            case 0:
                return (0, -1), 3
            case 1:
                return (-1, 0), 2
            case 2:
                return (0, 1), 1
            case 3:
                return (1, 0), 0
    else:
        match direction:
            case 0:
                return (0, 1), 1
            case 1:
                return (1, 0), 0
            case 2:
                return (0, -1), 3
            case 3:
                return (-1, 0), 2




def print_matrix(matrix):
    for row in matrix:
        print("".join(row))
    print()

main()