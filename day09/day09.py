import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *


def part1(data):
    pts = []
    mx = 0
    for line in data.strip().split('\n'):
        x, y = map(int, line.strip().split(','))
        pts.append((x, y))
    # print(pts)
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            # print(pts[i], pts[j])
            w = abs(pts[i][0] - pts[j][0])+1
            h = abs(pts[i][1] - pts[j][1])+ 1
            # print(w, h)
            if w * h > mx: 
                mx =  w * h
                # print(w, h)
    return mx


def part2(data):
    return 0


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
