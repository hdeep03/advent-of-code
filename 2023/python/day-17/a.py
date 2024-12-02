import sys
from heapq import heapify, heappop, heappush

direction_to_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N, E, S, W

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    cooling = []
    for line in data:
        cooling.append(list(line))
    
    n, m = len(cooling), len(cooling[0])
    start = (0, 0)
    end = (n-1, m-1)
    print(dijkstra(cooling, start, end))

def dijkstra(matrix, start, end):
    n, m  = len(matrix), len(matrix[0])
    queue = [(0, *start, 0, 0)] # dist, i, j, direction, count
    heapify(queue)
    visited = set() # (i, j)
    while queue:
        dist, i, j, direction, count = heappop(queue)
        if (i, j) == end and 4 <= count <= 10:
            return dist
        if (i, j, direction, count) in visited:
            continue
        visited.add((i, j, direction, count))
        invalids = [(direction + 2)%4] # Reversal condition
        if count == 3:
            invalids.append(direction) # 3 consecutive moves in same direction

        neighbors = get_neighbours(i, j, n, m, invalids)
        for x, y, d in neighbors:
            new_dist = dist + int(matrix[x][y])
            heappush(queue, (new_dist, x, y, d, count+1 if d == direction else 1))

def get_neighbours(x, y, n, m, invalid_directions=None):
    invalid_directions = set(invalid_directions if invalid_directions else [])
    proposed = []
    for i, (dx, dy) in enumerate(direction_to_delta):
        if i in invalid_directions:
            continue
        proposed.append((x+dx, y+dy, i))
    return [p for p in proposed if n > p[0] >= 0 and m > p[1] >= 0]

main()