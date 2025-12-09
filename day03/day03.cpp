#include "../aoc_utils.hpp"
#include <iostream>
#include <string>
#include <sstream>

namespace {
    std::string trim(const std::string& s) {
        const auto start = s.find_first_not_of(" \t\r\n");
        if (start == std::string::npos) return "";
        const auto end = s.find_last_not_of(" \t\r\n");
        return s.substr(start, end - start + 1);
    }

    std::string max_subsequence(const std::string& s, int k) {
        std::string result;
        result.reserve(k);

        const std::size_t n = s.size();
        std::size_t pos = 0;
        int remaining = k;

        while (remaining > 0 && pos < n) {
            std::size_t search_end = n - remaining;
            char best = '0';
            std::size_t best_idx = pos;

            for (std::size_t i = pos; i <= search_end; ++i) {
                char c = s[i];
                if (c > best) {
                    best = c;
                    best_idx = i;
                    if (best == '9') break;
                }
            }

            result.push_back(best);
            pos = best_idx + 1;
            --remaining;
        }

        return result;
    }
}

long long part1(const std::string& data) {
    long long total = 0;
    std::stringstream ss(data);
    std::string line;

    while (std::getline(ss, line)) {
        line = trim(line);
        if (line.size() < 2) continue;

        int mx = -1;
        for (std::size_t l = 0; l + 1 < line.size(); ++l) {
            int tens = line[l] - '0';
            for (std::size_t r = l + 1; r < line.size(); ++r) {
                int val = tens * 10 + (line[r] - '0');
                if (val > mx) mx = val;
            }
        }

        if (mx >= 0) total += mx;
    }

    return total;
}

long long part2(const std::string& data) {
    const int k = 12;
    long long total = 0;
    std::stringstream ss(data);
    std::string line;

    while (std::getline(ss, line)) {
        line = trim(line);
        if (line.size() < static_cast<std::size_t>(k)) continue;

        std::string selected = max_subsequence(line, k);
        if (!selected.empty()) {
            total += std::stoll(selected);
        }
    }

    return total;
}

int main() {
    std::string data = aoc::read_input("input.txt");
    std::cout << "Part 1: " << part1(data) << std::endl;
    std::cout << "Part 2: " << part2(data) << std::endl;
    return 0;
}
