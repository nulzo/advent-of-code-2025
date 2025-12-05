import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def parse(data):
    parts = data.split('\n\n')
    r,i = [],[]
    for line in parts[0].strip().split('\n'):
        s, e = map(int, line.split('-'))
        r.append((s, e))
    for l in parts[1].strip().split('\n'): i.append(int(l))
    return r, i

def part1(data):
    r, i = parse(data)
    c = 0
    for idv in i:
        for s, e in r:
            if s <= idv <= e: 
                c+=1
                break
    return c


def part2(data):
    c = 0
    for s, e in merge_intervals(parse(data)[0]): c += ((e - s) + 1)        
    return c


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    try:
        data = read_input(str(input_file))
    except FileNotFoundError:
        data = read_input("input.txt")
        
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
