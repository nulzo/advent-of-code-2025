import sys
import math
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *

def part1(data):
    pts = []
    prs = []
    uf = UnionFind()
    rc = Counter()
    
    for l in data.strip().split('\n'):
        pts.append(tuple(map(int, l.split(','))))

    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            prs.append((math.dist(pts[i], pts[j]), i, j))
            
    prs.sort(key=lambda x: x[0])
    
    for i in range(len(pts)): uf.find(i)
    for k in range(min(1000, len(prs))): uf.union(prs[k][1], prs[k][2])
    for i in range(len(pts)): rc[uf.find(i)] += 1
        
    sizes = sorted(rc.values(), reverse=True)
    
    if len(sizes) >= 3: return sizes[0] * sizes[1] * sizes[2]
    return math.prod(sizes)

def part2(data):
    return 0

if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
