import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    rolls = set()
    for r, l in enumerate(data.strip().split('\n')):
        for c, k in enumerate(l):
            if k == '@':
                rolls.add((r, c))
    tot = 0
    for r, c in rolls:
        s = 0
        for dr, dc in DIRS_8:
            d = ((r + dr), (c + dc))
            if d in rolls:
                s += 1
        if s < 4:
            tot += 1
    return tot


def part2(data):
    rolls = set()
    for r, l in enumerate(data.strip().split('\n')):
        for c, k in enumerate(l):
            if k == '@':
                rolls.add((r, c))
    rmd = 0
    while 1:
        rm = set()
        for r, c in rolls:
            s = 0
            for dr, dc in DIRS_8:
                if (r + dr, c + dc) in rolls:
                    s += 1            
            if s < 4:
                rm.add((r, c))
        if not rm: break
        rolls -= rm
        rmd += len(rm)
    return rmd


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
