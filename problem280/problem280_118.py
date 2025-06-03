def main():
    import sys
    readline = sys.stdin.buffer.readline

    import math
    import itertools

    n = int(readline())
    xy = [list(map(int, readline().split())) for _ in range(n)]

    c = list(itertools.combinations(range(n), 2))
    ans = 0
    for a, b in c:
        ans += ((xy[a][0] - xy[b][0])**2 + (xy[a][1] - xy[b][1])**2)**(1/2)
    print(ans*2*math.factorial(n-1)/math.factorial(n))

if __name__ == '__main__':
    main()