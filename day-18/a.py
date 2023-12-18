import sys

direction_to_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N, E, S, W
str_to_int = {"U": 0, "R": 1, "D": 2, "L": 3}
SIZE = 660
def main():
    data = sys.stdin.read()
    data = data.splitlines()
    instructions = []
    matrix = [[0]*SIZE for i in range(SIZE)]
    min_x, max_x, x = 0, 0, 0
    min_y, max_y, y = 0, 0, 0
    for line in data:
        direction, delta, color = line.split()
        direction = str_to_int[direction]
        if direction % 2 == 0:
            y += (direction-1)*-1*int(delta)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
        else:
            x += (direction-2)*-1*int(delta)
            max_x = max(max_x, x)
            min_x = min(min_x, x)
        instructions.append((direction, int(delta), color))
    #print(instructions, max_y, max_x, min_y, min_x, x, y)
    execute(instructions, matrix)
    flood_fill(matrix, SIZE//2, SIZE//2)
    print(count_ones(matrix))
    #print_matrix(matrix)

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
    

def execute(instructions, matrix):
    i, j = (SIZE//2, SIZE//2)
    for instruction in instructions:
        direction, delta, color = instruction
        di, dj = direction_to_delta[direction]
        for _ in range(delta):
            i += di
            j += dj
            matrix[i][j] = 9
    return matrix

def flood_fill(matrix, i, j):
    queue = [(i, j)]
    while queue:
        i, j = queue.pop(0)
        for di, dj in direction_to_delta:
            if 0 <= i+di < SIZE and 0 <= j+dj < SIZE and matrix[i+di][j+dj] == 0:
                matrix[i+di][j+dj] = 1
                queue.append((i+di, j+dj))

main()