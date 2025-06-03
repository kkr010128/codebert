from bisect import bisect_left
def main():
    n, dis, dam = map(int, input().split())
    mon = [list(map(int, input().split())) for _ in range(n)]
    mon.sort(key=lambda x: x[0])
    p = [v[0] for v in mon]
    imos = [0]*(n+1)
    dis = 2*dis + 1
    ans = 0
    for i in range(n):
        if 0 < i:
            imos[i] += imos[i-1]
        if imos[i] < mon[i][1]:
            tmp = (mon[i][1] - imos[i] + dam - 1) // dam
            ans += tmp
            tmp *= dam
            imos[i] += tmp
            idx = bisect_left(p, p[i]+dis)
            imos[idx] -= tmp
    print(ans)

if __name__ == "__main__":
    main()