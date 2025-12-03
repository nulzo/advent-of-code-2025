import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *


def part1(data):
    # sloppy 2 pointer, left for 10s digit, right for next highest preceeding
    tj = 0    
    for i in data.strip().split('\n'):
        i = i.strip()
        
        if len(i) < 2: continue
            
        d = [int(c) for c in i]
        
        l,r = 0,1
        r = 1
        mx = -1
        while l < len(d) - 1:
            t = d[l]
                
            r = l + 1
            while r < len(d):
                val = t * 10 + d[r]
                if val > mx:
                    mx = val
                r += 1
                
            l += 1

        tj += mx
    
    return tj


def part2(data):
    # setlled on greedy grabbing items while respecting OG order. probably will clean this later or try to make it better
    tj= 0
    for l in data.strip().split('\n'):
        r = []
        curr = l
        for i in range(12, 0, -1):
            # sliding window
            win = curr[:len(curr)-(i-1)]
            # important! it needs to always get the biggest in the windw
            r.append(max(win))
            # move to idx after the one above
            curr = curr[curr.find(max(win)) + 1:]
        tj += int(''.join(r))
    return tj


if __name__ == "__main__":
    try:
        data = read_input()
    except FileNotFoundError:
        print("Input file not found. Please create input.txt")
        sys.exit(1)

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
