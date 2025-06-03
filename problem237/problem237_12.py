def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    arms = []
    for i in range(N):
        x, l = map(int,input().split())
        t = min(x+l,10**9)
        s = max(x-l,0)
        arms.append((t,s))
    arms.sort()

    ans = 0
    tmp = -1

    for t,s in arms:
        if s >= tmp:
            tmp = t
            ans += 1

    print(ans)

main()