from typing import List, TypeAlias
import sys
from functools import cmp_to_key

Packet: TypeAlias = List["Packet"] | int


def splitLine(text: str) -> List[str]:
    depth = 0
    splits = []
    for i, ch in enumerate(text):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -=1
        elif ch == "," and depth == 0:
            splits.append(i)
    starts = [-1] + splits
    ends = splits + [len(text)]
    ret = []
    for s, e in zip(starts, ends):
        ret.append(text[s+1:e])
    return ret
    
def parseLine(text: str) -> Packet:
    if "[" not in text:
        return int(text)
    
    packet = list()
    text = text.strip()[1:-1]
    for segment in splitLine(text):
        if not segment:
            continue
        packet.append(parseLine(segment))
    return packet

def cmp(a: Packet, b: Packet) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return b-a
    if isinstance(a, list) and isinstance(b, list):
        for left, right in zip(a, b):
            res = cmp(left, right)
            if res < 0:
                return -1
            elif res > 0:
                return 1
        return len(b) - len(a)
    
    new_a = a
    new_b = b
    if isinstance(a, int):
        new_a = [a]
    else:
        new_b = [b]
    return cmp(new_a, new_b)

lines = sys.stdin.readlines()
i = 0
packets = []
while i < len(lines):
    if lines[i].strip():
        packets.append(parseLine(lines[i]))
    i+=1

packets.extend([[[2]], [[6]]])

div_idxs = [0, 0]

for i, packet in enumerate(sorted(packets, key=cmp_to_key(cmp), reverse=True), 1):
    if cmp(packet, [[2]]) == 0:
        div_idxs[0] = i
    elif cmp(packet, [[6]]) == 0:
        div_idxs[1] = i

print(div_idxs[0]*div_idxs[1])
# print(ct)
