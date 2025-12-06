#include "../aoc_utils.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

long long part1(const std::string& data) {
    std::string clean_data = data;
    clean_data.erase(std::remove(clean_data.begin(), clean_data.end(), '\n'), clean_data.end());
    
    auto items = aoc::split(clean_data, ',');
    long long inv = 0;
    
    for (const auto& item : items) {
        if (item.empty()) continue;
        auto parts = aoc::split(item, '-');
        if (parts.size() != 2) continue;
        
        long long start = std::stoll(parts[0]);
        long long end = std::stoll(parts[1]);
        
        for (long long n = start; n <= end; ++n) {
            std::string s = std::to_string(n);
            if (s.length() % 2 != 0) continue;
            size_t m = s.length() / 2;
            if (s.substr(0, m) == s.substr(m)) {
                inv += n;
            }
        }
    }
    return inv;
}

long long part2(const std::string& data) {
    std::string clean_data = data;
    clean_data.erase(std::remove(clean_data.begin(), clean_data.end(), '\n'), clean_data.end());
    
    auto items = aoc::split(clean_data, ',');
    long long inv = 0;
    
    for (const auto& item : items) {
        if (item.empty()) continue;
        auto parts = aoc::split(item, '-');
        if (parts.size() != 2) continue;
        
        long long start = std::stoll(parts[0]);
        long long end = std::stoll(parts[1]);
        
        for (long long n = start; n <= end; ++n) {
            std::string s = std::to_string(n);
            int ln = s.length();
            for (int l = 1; l <= ln / 2; ++l) {
                if (ln % l == 0) {
                    std::string p = s.substr(0, l);
                    int r = ln / l;
                    std::string repeated;
                    repeated.reserve(ln);
                    for(int k=0; k<r; ++k) repeated += p;
                    
                    if (repeated == s) {
                        inv += n;
                        break;
                    }
                }
            }
        }
    }
    return inv;
}

int main() {
    std::string data = aoc::read_input("input.txt");
    std::cout << "Part 1: " << part1(data) << std::endl;
    std::cout << "Part 2: " << part2(data) << std::endl;
    return 0;
}
