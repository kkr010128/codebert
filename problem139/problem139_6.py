def main():
    import sys
    input = lambda: sys.stdin.readline().rstrip()

    h1, m1, h2, m2, k = map(int, input().split())

    m = 60 - m1
    h1 += 1
    m += (h2 - h1)*60 + m2
    print(max(0, m - k))
main()