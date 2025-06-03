def solve(string):
    _, c = string.split()
    r = c.count("R")
    return str(c[:r].count("W"))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
