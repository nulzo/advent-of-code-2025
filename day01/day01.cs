using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        string data;
        try
        {
            string path = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "input.txt");
            
            if (!File.Exists(path))
            {
                path = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
            }
            
            data = File.ReadAllText(path);
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("input file not found.");
            return;
        }

        Console.WriteLine($"Part 1: {Part1(data)}");
        Console.WriteLine($"Part 2: {Part2(data)}");
    }

    static int Mod(int x, int m)
    {
        return (x % m + m) % m;
    }

    static int Part1(string data)
    {
        var lines = data.Trim().Split(new[] { '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
		int pos = 50;
		int count = 0;
        foreach (string str in lines)
        {
            string dir = str[..1];
            int movement = int.Parse(str[1..]);
            pos = Mod(pos + (dir == "R" ? movement : -movement), 100);
            count += pos == 0 ? 1 : 0;
        }
    
        return count;
    }

    static int Part2(string data)
    {
        var lines = data.Trim().Split(new[] { '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries);
        int cPos = 50;
        int cZero = 0;

        foreach (var line in lines)
        {
            string l = line.Trim();
            if (string.IsNullOrEmpty(l)) continue;

            char dir = l[0];
            int amt = int.Parse(l.Substring(1));

            if (dir == 'R')
            {
                cZero += (cPos + amt) / 100;
                cPos = Mod(cPos + amt, 100);
            }
            else if (dir == 'L')
            {
                int wrapCount = amt / 100;
                int remainderCheck = (cPos < (amt % 100)) ? 1 : 0;
                cZero += wrapCount + remainderCheck;
                cPos = Mod(cPos - amt, 100);
            }
        }

        return cZero;
    }
}