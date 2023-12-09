import sys

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    x = 0
    for line in data:
        x+= (process(line))
    print(x)

def process(line: str) -> int:
    starting_elements = [int(x) for x in line.split(' ')]
    layers = [starting_elements]
    while any(layers[-1]):
        new_layer = []
        for i in range(1, len(layers[-1])):
            new_layer.append(layers[-1][i] - layers[-1][i-1])
        layers.append(new_layer)
    prop = 0
    for i in range(len(layers) - 1, -1, -1):
        prop = layers[i][0] - prop
    return prop

main()