def solve(string):
    a = int(string)
    return str(a + a**2 + a**3)                                                                                         

if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
