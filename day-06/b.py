import sys
import math

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    tdata = data[0].split(":")[1]
    ddata = data[1].split(":")[1]
    time = int("".join([x for x in tdata.split(" ") if x != ""]))
    distance = int("".join([x for x in ddata.split(" ") if x != ""]))
    print(math.sqrt(time**2 - 4*distance))

main()