import sys
from typing import List

def main():
    data = sys.stdin.read().splitlines()
    seeds = [int(x) for x in data[0].split(":")[1].split(" ") if x != ""]
    seeds, rng = seeds[::2], seeds[1::2]

    data = "\n".join(data[2:])
    guides = {} # category name
    for block in data.split("\n\n"):
        name = block.split(":")[0].rstrip(" map")
        guides[name] = [(z) for z in block.split(":")[1].split("\n") if z != ""]
        guides[name] = [x.split(" ") for x in guides[name]]
        guides[name] = [[int(x) for x in y] for y in guides[name]]

    current, end = "seed", "location"
    intervals = [(seeds[i], rng[i]) for i in range(len(seeds))]
    while current != end:
        for k, v in guides.items():
            if k.startswith(current):
                new_intervals = []
                for interval in intervals:
                    new_intervals.extend(computeRule(interval[0], interval[1], v))
                current = k.split("-")[-1]
                intervals = new_intervals
                break
    print(min(intervals, key=lambda x: x[0])[0])


def computeRule(input_start: int, input_range: int, guide: list) -> List[int]:
    output_intervals = []
    for dest, start, rng in sorted(guide, key=lambda x: x[1]):
        if input_start >= start and input_start < start + rng:
            end = min(start + rng, input_start + input_range)
            new_rng = end - input_start
            new_start = dest + input_start - start
            output_intervals.append((new_start, new_rng))
            
            if end == input_start + input_range:
                input_range -= new_rng
                break
            
            input_start = end
            input_range -= new_rng
    if input_range != 0:
        output_intervals.append((input_start, input_range))
    return output_intervals

main()