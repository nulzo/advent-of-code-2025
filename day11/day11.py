import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from aoc_utils import *


def part1(data):
    lines = data.split('\n')
    g = {}
    for l in lines:
        node, raw = l.split(':')
        g[node] = raw.split()

    s, e = "you", "out"
    v = set()

    def dfs(node):
        if node == e: return 1
        v.add(node)
        tot = 0
        for i in g.get(node, []):
            tot += dfs(i)
        v.remove(node)
        return tot

    return dfs(s)


def part2(data):
    g = {}
    for l in data.split("\n"):
        node, raw = l.split(':')
        g[node] = raw.split()

    s, e = "svr", "out"
    memo = {}
    v = set()
    def dfs(node, has_dac, has_fft):
        if node == "dac":
            has_dac = True
        if node == "fft":
            has_fft = True

        if node == e: return 1 if (has_dac and has_fft) else 0

        if (node, has_dac, has_fft) in memo: return memo[(node, has_dac, has_fft)]

        v.add(node)
        # print(v)
        tot = 0
        for i in g.get(node, []): tot += dfs(i, has_dac, has_fft)
        v.remove(node)
        memo[(node, has_dac, has_fft)] = tot
        # print(tot)
        return tot

    return dfs(s, False, False)


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
