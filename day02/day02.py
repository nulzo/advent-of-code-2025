import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    items = data.replace('\n', '').split(',')    
    inv = 0
    
    for r in items:
        if not r: continue
        start, end = map(int, r.split('-'))
        
        for n in range(start, end + 1):
            s = str(n)
            if len(s) % 2 != 0: continue
            m = len(s) // 2
            if s[:m] == s[m:]:
                inv += n
                
    return inv

def part2(data):
    items = data.replace('\n', '').split(',')    
    inv = 0
    
    for r in items:
        if not r: continue
        start, end = map(int, r.split('-'))
        for n in range(start, end + 1):
            s = str(n)
            ln = len(s)
            for l in range(1, ln // 2 + 1):
                if ln % l == 0:
                    pattern = s[:l]
                    repeats = ln // l
                    if pattern * repeats == s:
                        inv += n
                        break
    return inv


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
