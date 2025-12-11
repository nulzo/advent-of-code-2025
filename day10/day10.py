import sys
from pathlib import Path
import re

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    tot = 0
    for l in data.strip().splitlines():
        lts = re.search(r'\[([.#]+)\]', l).group(1)
        tg_msk = 0
        for i, ch in enumerate(lts):
            if ch == '#':
                tg_msk |= (1 << i)

        bt_msk = []
        for group in re.findall(r'\(([\d,]+)\)', l):
            msk = 0
            for p in map(int, group.split(',')):
                msk |= 1 << p
            bt_msk.append(msk)

        m = len(bt_msk)
        b = sys.maxsize
        for sub in range(1 << m):
            p = sub.bit_count()
            if p >= b:
                continue
            s = 0
            for idx, bm in enumerate(bt_msk):
                if (sub >> idx) & 1: s ^= bm
            if s == tg_msk: b = p
        tot += b if b < sys.maxsize else 0
    return tot

def part2(data):
    return 0

if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
