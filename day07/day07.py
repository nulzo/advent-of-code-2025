import sys
from pathlib import Path
from collections import defaultdict

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    g = [list(line) for line in data.split('\n')]
    cols = {[c for c in range(len(g[0])) if g[0][c] == 'S'][0]}
    tot = 0
    for r in range(len(g)):
        nxt = set()
        for c in cols:
            ok = g[r][c] != '^'
            nxt.add(c) if ok else nxt.update([c - 1, c + 1])
            if ok: tot += 1
        cols = nxt
    return tot


def part2(data):
    return 0


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
