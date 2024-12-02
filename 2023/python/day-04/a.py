import sys

def main():
    #data = sys.stdin.read()
    ct = 0
    for line in sys.stdin:
        line = line.split(":")[1]
        first_set, second_set = line.split("|")
        s2 = set()
        for x in second_set.split(" "):
            try:
                x = int(x)
                s2.add(x)
            except:
                continue
        points = 0
        second_set = s2
        for x in first_set.split():
            try:
                x = int(x)
            except:
                continue
            if x in second_set:
                if points == 0:
                    points = 1
                else:
                    points *=2 
        print(points)
        ct += points

    print(ct)
        

main()