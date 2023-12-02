import sys

def main():
    ct = 0
    for line in sys.stdin:
        line = line.strip()
        id = line.split(":")[0].split(" ")[1]
        subgame = line.split(":")[1].split(";")
        flag = False
        for chunk in subgame:
            vals = {}
            for x in chunk.split(","):
                vals[x.strip().split(" ")[1]] = int(x.strip().split(" ")[0])
            if vals.get("blue", 0) > 14 or vals.get("red", 0) > 12 or vals.get("green", 0) > 13:
                flag = True
                break
        if not flag:
            ct+=int(id)
    print(ct)
        
main()