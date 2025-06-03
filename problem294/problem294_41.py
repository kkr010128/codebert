import bisect
def main2():
    N = int(input())
    L = list(map(int, input().split()))
    L = sorted(L)

    ans = 0
    for i in range(len(L) - 2):
        for j in range(i + 1, len(L) - 1):
            ab = L[i] + L[j]
            r = bisect.bisect_left(L, ab)
            l = j + 1
            ans += r - l

    print(ans)

if __name__ == "__main__":
    main2()