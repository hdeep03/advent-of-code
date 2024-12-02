import sys

cubes = set()

for line in sys.stdin.readlines():
    x, y, z = map(int, line.split(","))
    cubes.add((x, y, z))

area = 6 * len(cubes)

for x, y, z in cubes:
    offsets = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for dx, dy, dz in offsets:
        if (x+dx, y+dy, z+dz) in cubes:
            area -= 1
print(area)

 