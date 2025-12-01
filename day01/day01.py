import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    """
    count how many times we land exactly on 0

    - start at position 50 on a cyclical track from 0 to 99
    - each move is either right or left by some amount
    - count each time our final position after a move is exactly 0
    """
    lines = data.strip().split('\n')
    c_pos, c_zero = 50, 0

    for l in lines:
        l = l.strip()
        if not l: continue

        dir, amt = l[0], int(l[1:])
        # move to wrap around, modulating to find where we end up
        c_pos = (c_pos + (1 if dir == 'R' else -1) * amt) % 100
        # increment the count if we're on a 0
        c_zero += 1 if not c_pos else 0

    return c_zero


def part2(data):
    """
    count how many times we pass thru 0 during moves

    - same as first one with starting pos and size
    - count every time we pass thru 0
    - important! it can include large moves that can pass thru more than once
    """
    lines = data.strip().split('\n')
    c_pos, c_zero = 50, 0

    for l in lines:
        l = l.strip()
        if not l: continue
        dir, amt = l[0], int(l[1:])
        if dir == 'R':
            # moving right
            # (c_pos + amt) // 100 counts how many times we crossed 0
            # i.e. if pos 50, move 60 right -> 50+60=110, 110//100=1
            c_zero += (c_pos + amt) // 100
            c_pos = (c_pos + amt) % 100
        elif dir == 'L':
            # moving left
            # amt // 100 + (1 if c_pos < amt % 100 else 0)
            # check full wraps from large jumps, then check if we crossed 0
            # i.e. if pos 10, move 20 left -> crosses 1 if 10 < 20%100=20
            c_zero += amt // 100 + (1 if c_pos < amt % 100 else 0)
            c_pos = (c_pos - amt) % 100

    return c_zero


if __name__ == "__main__":
    try:
        data = read_input()
    except FileNotFoundError:
        print("input file not found.")
        sys.exit(1)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
