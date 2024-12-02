import sys
from math import gcd

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    instructions = data[0]
    adj_list = {}
    for x in data[1:]:
        if x != '':
            start = x.split('=')[0].strip() 
            other = x.split('=')[1].strip()
            l, r = other[1:-1].split(',')
            l = l.strip()
            r = r.strip()
            adj_list[start] = (l, r)
    location = "AAA"
    ct = 0
    while location != "ZZZ":
        instruction = instructions[ct % len(instructions)]
        location = adj_list[location][0] if instruction == 'L' else adj_list[location][1]
        ct += 1
    print(ct)



main()