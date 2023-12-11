import sys
from heapq import heapify, heappop, heappush
from tqdm import tqdm, trange

scale_factor = 10**6

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    has_galaxy = [[False] * len(data[0]) for _ in range(len(data))]
    old_matrix = [[0]*len(data[0]) for _ in range(len(data))]
    for i, line in enumerate(data):
        for j, x in enumerate(line):
            if x == "#":
                old_matrix[i][j] = 1
                has_galaxy[i][j] = True
        print(line)
    rows = [any(has_galaxy[i]) for i in range(len(has_galaxy))]
    cols = [any(has_galaxy[i][j] for i in range(len(has_galaxy))) for j in range(len(has_galaxy[0]))]

    positions = []
    for i, row in enumerate(old_matrix):
        for j, x in enumerate(row):
            if x == 1:
                positions.append((i, j))
    total_dist = 0

    for i in trange(len(positions)-1):
        x = positions[i]
        dmat = compute_distance(x, rows, cols)
        for j in range(i+1, len(positions)):
            y = positions[j]
            total_dist += dmat[y[0]][y[1]]
    print(total_dist)

def print_matrix(matrix):
    for row in matrix:
        for x in row:
            print(x, end="")
        print()

def compute_distance(x, rows, cols):
    queue = [(0, x)]
    heapify(queue)
    visited = set([x])
    distance_matrix = [[float("inf")]*len(cols) for _ in range(len(rows))]
    while queue:
        dist, current = heappop(queue)
        distance_matrix[current[0]][current[1]] = min(dist, distance_matrix[current[0]][current[1]])
        for neighbor in get_neighbors(current, len(rows), len(cols)):
            if neighbor not in visited:
                extra_jump = 1
                if neighbor[0] == current[0]:
                    # x-move
                    if not cols[neighbor[1]]:
                        extra_jump = scale_factor
                else:
                    # y-move
                    if not rows[neighbor[0]]:
                        extra_jump = scale_factor
                visited.add(neighbor)
                heappush(queue, (extra_jump+dist, neighbor))
    return distance_matrix

def get_neighbors(loc, num_rows, num_cols):
    x, y = loc
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < num_rows-1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < num_cols-1:
        neighbors.append((x, y+1))
    return neighbors
        
main()