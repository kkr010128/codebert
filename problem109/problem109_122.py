def solve():
    N = int(input())
    cnt = {}
    for i in range(N):
        result = input()
        cnt[result] = cnt.get(result, 0) + 1
    for result in ("AC", "WA", "TLE", "RE"):
        print("{} x {}".format(result, cnt.get(result, 0)))

if __name__ == "__main__":
    solve()