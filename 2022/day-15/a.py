from typing import Tuple, Optional, List
from tqdm import trange
import sys


def manhattan_dist(coord1, coord2):
    dist = 0
    for c1, c2 in zip(coord1, coord2):
        dist += abs(c2 - c1)
    return dist

def project(x_src, y_src, dist, y_tgt) -> Optional[Tuple[int, int]]:
    # returns the min and max possible range inclusive, else none
    remainder = dist - abs(y_tgt - y_src)
    if remainder <= 0:
        return None
    return (x_src - remainder, x_src + remainder)


def parseLine(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    def get_coords(rs: str) -> Tuple[int, int]:
        rs = rs.split("x=", 1)[1]
        x_1 = int(rs.split(",", 1)[0])
        rs = rs.split("y=", 1)[1]
        y_1 = int(rs.split(":", 1)[0])
        return (x_1, y_1), rs.split(":", 1)[1]
    (x1, y1), res = get_coords(line)
    (x2, y2), _ = get_coords(res+":")
    return (x1, y1), (x2, y2)

sensors = [] # Triplet of x,y,man_dist
beacons = []
for line in sys.stdin.readlines():
    sensor_pos, beacon_pos = parseLine(line)
    beacons.append((beacon_pos[0], beacon_pos[1]))
    dst = manhattan_dist(sensor_pos, beacon_pos)
    sensors.append((*sensor_pos, dst))


def merge_segments(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    ranges = sorted(ranges, key=lambda x: x[0])
    i = 0
    ret = []
    while i < len(ranges):
        curr_range = ranges[i]
        if ret and ret[-1][1] >= curr_range[0] - 1:
            ret[-1] = (ret[-1][0], max(ret[-1][1], curr_range[1]))
        else:
            ret.append(curr_range)
        i+=1

    return ret

def get_results(y):
    segments = []
    for s_x, s_y, dist in sensors:
        res = project(s_x, s_y, dist, y)
        if not res:
            continue
        segments.append(res)

    res = merge_segments(segments)
    return res

for y in trange(0, 4_000_001):
    res = get_results(y=y)
    if len(res) != 1:
        print(res)
        print(y)

