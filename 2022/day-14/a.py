import sys


walls = set() # (x, y) coord of the wall

lines = sys.stdin.readlines()
for line in lines:
    coords = list(map(lambda x: map(int, x.split(",")), map(str.strip, line.split("->"))))
    x, y = coords[0]
    for x_p, y_p in coords[1:]:
        min_x = min(x, x_p)
        min_y = min(y, y_p)
        max_x = max(x, x_p)
        max_y = max(y, y_p)
        for x_w in range(min_x, max_x+1):
            for y_w in range(min_y, max_y + 1):
                walls.add((x_w, y_w))
        x = x_p
        y= y_p

max_y = max(map(lambda x: x[1], walls))

def simulate(source_x, source_y) -> int:
    curr_pos = (source_x, source_y)
    iters = 0
    while curr_pos[1] < max_y + 2:
        y_p = curr_pos[1] + 1
        moved = False
        for dx in [0, -1, 1]:
            x_p = curr_pos[0] + dx
            if (x_p, y_p) not in walls:
                curr_pos = (x_p, y_p)
                moved = True
                break
        if not moved:
            walls.add(curr_pos)
            print(curr_pos)
            return iters
        else:
            iters += 1
    walls.add((curr_pos[0], curr_pos[1]-1))
    return -1 # sand oor

res = simulate(500, 0)
ct = 0
while (500, 0) not in walls:
    ct += 1
    res = simulate(500, 0)
print(ct+1)