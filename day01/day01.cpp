#include "../aoc_utils.hpp"

// thanks to @spice for showing me how to do this and
// how to write good c++! :dog_smiling: /s
using namespace std;

long long part1(const vector<string> &lines)
{
    long long c_pos = 50;
    long long c_zero = 0;

    for (const string &l : lines)
    {
        if (l.empty())
            continue;

        char dir = l[0];
        int amt = stoi(l.substr(1));

        if (dir == 'R')
        {
            c_pos = (c_pos + amt) % 100;
        }
        else
        {
            c_pos = (c_pos - amt) % 100;
            if (c_pos < 0)
                c_pos += 100;
        }

        if (c_pos == 0)
            c_zero++;
    }
    return c_zero;
}

long long part2(const vector<string> &lines)
{
    long long c_pos = 50;
    long long c_zero = 0;

    for (const string &l : lines)
    {
        if (l.empty())
            continue;

        char dir = l[0];
        int amt = stoi(l.substr(1));
        long long cnt = amt;

        if (dir == 'R')
        {
            long long dist = (100 - c_pos) % 100;
            if (dist == 0)
                dist = 100;

            if (cnt >= dist)
            {
                c_zero++;
                cnt -= dist;
                c_zero += cnt / 100;
            }
            c_pos = (c_pos + amt) % 100;
        }
        else if (dir == 'L')
        {
            long long dist = c_pos;
            if (dist == 0)
                dist = 100;

            if (cnt >= dist)
            {
                c_zero++;
                cnt -= dist;
                c_zero += cnt / 100;
            }

            c_pos = (c_pos - amt) % 100;
            if (c_pos < 0)
                c_pos += 100;
        }
    }
    return c_zero;
}

int main(int argc, char *argv[])
{
    string filename = "input.txt";
    vector<string> lines = aoc::read_lines(filename);
    cout << "Part 1: " << part1(lines) << endl;
    cout << "Part 2: " << part2(lines) << endl;
    return 0;
}
