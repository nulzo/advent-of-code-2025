#include "../aoc_utils.hpp"
#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <utility>

namespace
{
    using Pos = std::pair<int, int>;
    const std::vector<Pos> DIRS = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
};

std::string trim(const std::string &s)
{
    const auto start = s.find_first_not_of(" \t\r\n");
    if (start == std::string::npos)
        return "";
    const auto end = s.find_last_not_of(" \t\r\n");
    return s.substr(start, end - start + 1);
}

std::set<Pos> parse_rolls(const std::string &data)
{
    std::set<Pos> rolls;
    std::stringstream ss(data);
    std::string line;
    int r = 0;
    while (std::getline(ss, line))
    {
        line = trim(line);
        if (line.empty())
        {
            ++r;
            continue;
        }
        for (int c = 0; c < static_cast<int>(line.size()); ++c)
        {
            if (line[c] == '@')
            {
                rolls.insert({r, c});
            }
        }
        ++r;
    }
    return rolls;
}

int neighbor_count(const std::set<Pos> &rolls, const Pos &p)
{
    int count = 0;
    for (const auto &d : DIRS)
    {
        Pos n{p.first + d.first, p.second + d.second};
        if (rolls.find(n) != rolls.end())
        {
            ++count;
        }
    }
    return count;
}

long long part1(const std::string &data)
{
    auto rolls = parse_rolls(data);
    long long total = 0;
    for (const auto &p : rolls)
    {
        int neighbors = neighbor_count(rolls, p);
        if (neighbors < 4)
        {
            ++total;
        }
    }
    return total;
}

long long part2(const std::string &data)
{
    auto rolls = parse_rolls(data);
    long long removed = 0;

    while (true)
    {
        std::vector<Pos> to_remove;
        to_remove.reserve(rolls.size());

        for (const auto &p : rolls)
        {
            int neighbors = neighbor_count(rolls, p);
            if (neighbors < 4)
            {
                to_remove.push_back(p);
            }
        }

        if (to_remove.empty())
        {
            break;
        }

        for (const auto &p : to_remove)
        {
            rolls.erase(p);
        }
        removed += static_cast<long long>(to_remove.size());
    }

    return removed;
}

int main()
{
    std::string data = aoc::read_input("input.txt");
    std::cout << "Part 1: " << part1(data) << std::endl;
    std::cout << "Part 2: " << part2(data) << std::endl;
    return 0;
}
