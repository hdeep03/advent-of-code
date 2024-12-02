import sys

def main():
    data = sys.stdin.read()
    instructions, part_values = data.split("\n\n")
    
    lookup = {}
    for line in instructions.splitlines(): # Instructions
        name, procedure = line.split("{")
        procedure = procedure[:-1]
        lookup[name] = procedure.split(",")

    parts = []
    for line in part_values.splitlines(): # parts
        line = line[1:-1]
        rule = {}
        for attribute in line.split(","):
            key, value = attribute.split("=")
            rule[key] = int(value)
        parts.append(rule)

    x = 0
    for part in parts:
        if solve(part, lookup):
            x+=(get_part_sum(part))
    print(x)

def get_part_sum(part):
    return sum(part.values())

def solve(part, lookup):
    currstate = "in"
    while currstate != "A" and currstate != "R":
        procedure = lookup[currstate]
        flag = False
        for proc in procedure[:-1]:
            attribute = proc[0]
            op = proc[1]
            value = int(proc[2:].split(":")[0])
            new_state = proc.split(":")[1]
            if part[attribute] > value and op == ">" or part[attribute] < value and op == "<":
                currstate = new_state
                flag = True
                break
        if not flag:
            currstate = procedure[-1]

    return currstate == "A"


main()