def solve(string):
    s, t = string.split()
    return str(len(s) - sum(_s == _t for _s, _t in zip(s, t)))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))