import sys

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

    # Expand the old_matrix by adding extra rows and columns
    new_matrix = []
    for i, row in enumerate(rows):
        new_matrix.append(old_matrix[i][:])
        if not row:
            new_matrix.append(old_matrix[i][:])
    offset = 0
    for i, col in enumerate(cols):
        if not col:
            for row in new_matrix:
                row.insert(i+offset, 0)
            offset += 1
    for row in new_matrix:
        for x in row:
            print(x, end="")
        print()

    positions = []
    for i, row in enumerate(new_matrix):
        for j, x in enumerate(row):
            if x == 1:
                positions.append((i, j))
    total_dist = 0
    for x in positions:
        for y in positions:
            if x != y:
                total_dist += abs(x[0]-y[0]) + abs(x[1]-y[1])
    print(total_dist//2)



        
main()