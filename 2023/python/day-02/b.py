import sys

def main():
    ct = 0
    for line in sys.stdin:
        line = line.strip()
        id = line.split(":")[0].split(" ")[1]
        subgame = line.split(":")[1].split(";")
        max_red, max_blue, max_green = 0, 0, 0
        for chunk in subgame:
            vals = {}
            for x in chunk.split(","):
                vals[x.strip().split(" ")[1]] = int(x.strip().split(" ")[0])
            max_blue = max(max_blue, vals.get("blue", 0))
            max_red = max(max_red, vals.get("red", 0))
            max_green = max(max_green, vals.get("green", 0))
        ct+=max_blue*max_red*max_green
    print(ct)
        
main()