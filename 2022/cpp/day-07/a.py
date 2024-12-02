import sys

class Node:
    def __init__(self, size, parent):
        self.parent = parent
        self.children = {} # map of children if directory
        self.sz = size # size is 0 if directory


def update_ls(start, lines, ptr):
    while start < len(lines) and lines[start][0] != "$":
        size, name = lines[start].split()
        sz = 0 if size == "dir" else int(size)
        if name not in ptr.children:
            new_node = Node(sz, ptr)
            ptr.children[name] = new_node
        start += 1
    return start

contents = sys.stdin.read()
lines = contents.splitlines()
ptr = Node(0, None)
root = ptr
i = 0
while i < len(lines):
    line = lines[i]
    argv = line[1:].split()
    if argv[0] == "ls":
        i = update_ls(i+1, lines, ptr)
    else:
        # cd cmd
        tgt = argv[1]
        if tgt == "/":
            ptr = root
        elif tgt == "..":
            ptr = ptr.parent
        else:
            ptr = ptr.children[tgt]
        i+=1

sizes = {} # map from directory unique name to its size

def dfs(node: Node, name: str) -> None:
    sz = 0
    for suffix, child in node.children.items():
        if child.sz == 0:
            dfs(child, name+suffix)
            sz += sizes[name+suffix]
        else:
            sz += child.sz
    sizes[name] = sz

dfs(root, "/")
rm_needed = (sizes["/"] - 40_000_000)
min_val = 10**9
for size in sizes.values():
    if size > rm_needed and size < min_val:
        min_val = size
print(min_val) 
        
