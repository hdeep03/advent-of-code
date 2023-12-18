import sys

direction_to_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d2d = lambda x: (x+1) % 4
def main():
    data = sys.stdin.read()
    data = data.splitlines()
    instructions = []
    for line in data:
        _, _, color = line.split()
        color = color[2:-1]
        direction = d2d(int(color[-1]))
        delta = int(color[:-1], 16)
        instructions.append((direction, int(delta)))
    ct = 0
    for x in instructions:
        ct += x[1]
    print(int(shoelace(get_points(instructions)[:-1]))+ct//2 + 1)

def count_ones(matrix):
    count = 0
    for row in matrix:
        for cell in row:
            if cell == 1 or cell == 9:
                count += 1
    return count

def print_matrix(matrix):
    for row in matrix:
        print("".join(map(str, row)))
    

def shoelace(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2
    return area

def get_points(instructions):
    points = [(0, 0)]
    for direction, delta in instructions:
        i, j = points[-1]
        di, dj = direction_to_delta[direction]
        points.append((i+di*delta, j+dj*delta))
    return points

main()