import sys

def main():
    data = sys.stdin.read()
    n, m = len(data.splitlines()[0]), len(data.splitlines())
    symbol_table = {}
    for row, line in enumerate(data.splitlines()):
        for col, char in enumerate(line):
            if char == '*':
                symbol_table[(col, row)] = []
    ct = 0
    for row, line in enumerate(data.splitlines()):
        i = 0
        while i < n:
            buff = ''
            while i < n and line[i].isdigit():
                buff += line[i]
                i += 1
            if buff:
                idx_left = i - len(buff)
                idx_right = i
                flag = False
                for x in range(idx_left-1, idx_right+1):
                    for y in range(row-1, row+2):
                        if (x, y) in symbol_table:
                            symbol_table[(x, y)].append(int(buff))
            i+=1
    for key, value in symbol_table.items():
        if len(value) == 2:
            ct += value[0] * value[1]
    print(ct)


    

main()