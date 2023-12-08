import sys
from math import gcd

def main():
    data = sys.stdin.read().splitlines()
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
    locs = [x for x in adj_list if x[-1] == "A"]
    first_z = [0]*len(locs)
    ct = 0
    while not all(first_z):
        instruction = instructions[ct % len(instructions)]
        for i, loc in enumerate(locs):
            l, r = adj_list[loc]
            if instruction == 'L':
                loc = l
            else:
                loc = r
            locs[i] = loc
            if first_z[i] == 0 and loc[-1] == 'Z':
                first_z[i] = ct+1
        ct += 1
    lcm = 1
    for i in first_z:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)
main()