import sys
from collections import deque

lines = sys.stdin.read().splitlines()
n, m = len(lines), len(lines[0])
matrix = [[0] * m for _ in range(n)]
start = (0, 0)
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == "#":
            matrix[i][j] = 1
        if ch == "S":
            start = (i , j)


def is_valid(i, j) -> bool:
    bounds = 0 <= i < n and 0 <= j < m
    return bounds and matrix[i][j] == 0

visited = set([start])
queue = deque([(0, *start)])
soln = set()
while queue:
    depth, i, j = queue.pop()
    if depth > 64:
        break
    if depth % 2 == 0:
        soln.add((i, j))
    
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in deltas:
        coords = i + di, j + dj
        if coords not in visited and is_valid(*coords):
            queue.appendleft((depth + 1, *coords))
            visited.add(coords)
print(len(soln))