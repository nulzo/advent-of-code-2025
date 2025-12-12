import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    a = 0
    for line in data.strip().split('\n\n')[-1].splitlines():
        w, h = map(int, line.split(": ")[0].split("x"))
        if sum(map(int, line.split(": ")[1].split())) <= (w // 3) * (h // 3): a += 1
    return a


def part2(data):
    """
    No extra star for today
    """
    return 0


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
