def solve(string):
    return str(max(map(len, string.split("S"))))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
