import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    lines = data.strip().split('\n')
    c_pos, c_zero = 50, 0
    
    for l in lines:
        l = l.strip()
        if not l: continue
        
        dir, amt = l[0], int(l[1:])
        c_pos = (c_pos + (1 if dir == 'R' else -1) * amt) % 100
        # print("chat, we have position", c_pos)
        if c_pos == 0:
            print("erm, we just got 0")
            
        c_zero += 1 if not c_pos else 0
    
    return c_zero


def part2(data):
    lines = data.strip().split('\n')
    c_pos, c_zero = 50, 0
    
    for l in lines:
        l = l.strip()
        if not l: continue
        dir, amt = l[0], int(l[1:])
        cnt = amt
        if dir == 'R':
            dist = (100 - c_pos) % 100
            if dist == 0: dist = 100
            
            if cnt >= dist:
                c_zero += 1
                cnt -= dist
                c_zero += cnt // 100
                # print("erm...", cnt, dist)
                # print("chat, we cnt 0", c_zero)
                
            c_pos = (c_pos + amt) % 100
            
        elif dir == 'L':
            dist = c_pos
            if dist == 0: dist = 100
            
            if cnt >= dist:
                c_zero += 1
                cnt -= dist
                c_zero += cnt // 100
            
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
