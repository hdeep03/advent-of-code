import sys
from tqdm import tqdm
from functools import cache

def main():
    data = sys.stdin.read()
    data = data.splitlines()
    x = 0
    for line in tqdm(data):
        print(parse(line))
        #x+= count_arrangements(*parse_b(line))
        x+= count_arrangements(*parse(line))
       #exit()
    print(x)

def count_arrangements(row, group_sizes): # # too slow for b
    def is_valid(arrangement):
        groups = []
        count = 0
        for spring in arrangement:
            if spring == '#':
                count += 1
            elif count > 0:
                groups.append(count)
                count = 0
        if count > 0:
            groups.append(count)
        return tuple(groups) == group_sizes

    def add_at_index(arrangement, index, spring):
        return arrangement[:index] + spring + arrangement[index + 1:]
    @cache
    def count_recursive(arrangement, index):
        if index >= len(arrangement):
            return 1 if is_valid(arrangement) else 0
        if arrangement[index] != '?':
            return count_recursive(arrangement, index + 1)
        count_dot = count_recursive(add_at_index(arrangement, index, "."), index + 1)
        count_hash = count_recursive(add_at_index(arrangement, index, "#"), index + 1)
        return count_dot + count_hash
    return count_recursive(row, 0)

def parse(line):
    data, nums = line.split(" ")
    nums = tuple(map(int, nums.split(",")))
    return data, nums

def parse_b(line):
    data, nums = line.split(" ")
    return "?".join([data]*5), tuple(map(int, nums.split(",")))*5

main()