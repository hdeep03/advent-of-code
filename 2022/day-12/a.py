import sys
from collections import deque

lines = sys.stdin.readlines()
heights = [ [0]*len(lines[0]) for _ in range(len(lines))] # 2d matrix representing heights

s_ptrs = []
e_ptr = (0, 0)

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        heights[i][j] = ord(ch)
        if ch == "S" or ch == "a":
            s_ptrs.append((i, j))
            heights[i][j] = ord("a")
        elif ch == "E":
            e_ptr = (i, j)
            heights[i][j] = ord("z")


def is_valid(i, j, curr_ele) -> bool:
    if i >= len(heights) or i < 0:
        return False
    if j >= len(heights[0]) or j < 0:
        return False
    new_ele = heights[i][j]
    return new_ele - curr_ele <= 1

def dfs(starts, end) -> int:
    queue = deque([(0, *start) for start in starts]) # (steps, i, j)
    visited = set() # tuples of visited (i, j) coords
    while queue:
        dist, i, j = queue.pop()
        curr_height = heights[i][j]
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in offsets:
            new_coords = (i + di, j + dj)
            if new_coords not in visited and is_valid(*new_coords, curr_height):
                visited.add(new_coords)
                if end == new_coords:
                    return dist + 1
                queue.appendleft((dist + 1, *new_coords))
    return -1

print(dfs(s_ptrs, e_ptr))
