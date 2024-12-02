import sys

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    seeds = [int(x) for x in data[0].split(":")[1].split(" ") if x != ""]
    data = "\n".join(data[2:])
    guides = {} # category name
    for block in data.split("\n\n"):
        name = block.split(":")[0].rstrip(" map")
        guides[name] = [(z) for z in block.split(":")[1].split("\n") if z != ""]
        guides[name] = [x.split(" ") for x in guides[name]]
        guides[name] = [[int(x) for x in y] for y in guides[name]]
    min_location = float("inf")
    for value in seeds:
        current = "seed"
        end = "location"
        while current != end:
            for k in guides:
                if k.startswith(current):
                    value = computeRule(value, guides[k])
                    current = k.split("-")[-1]
                    break
            #print(value)
        min_location = min(min_location, value)
    print(min_location)
                

def computeRule(value: int, guide: list) -> int:
    for dest, start, rng in guide:
        if value >= start and value <= start + rng:
            return dest + value - start
    return value

main()