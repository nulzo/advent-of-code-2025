import sys, math
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    s=0
    for c in zip(*[l.split() for l in data.splitlines()]):
        s+={'+':sum,'*':math.prod}[c[-1]](map(int,c[:-1]))
    return s

def part2(data):
    s,x,o,L=0,[],0,data.splitlines()
    for c in list(zip(*[l.ljust(max(map(len,L)))for l in L]))+[()]:
        n=''.join(filter(str.isdigit,c))
        if n:
            if not o:o={'+':sum,'*':math.prod}[c[-1]]
            x+=[int(n)]
        elif o:s+=o(x);x=[];o=0
    return s

if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
