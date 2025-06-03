def calc(day, i, m, d, S, c):
    m += S[day][i]
    d[i] = day
    for i in range(26):
        m -= c[i] * (day - d[i])
    return m, d
def main():
    D = int(input())
    c = list(map(int, input().split()))
    S = []
    d = {i:-1 for i in range(26)}
    for _ in range(D):
        s = list(map(int, input().split()))
        S.append(s)
    m = 0
    for i in range(D):
        t = int(input())
        t -= 1
        m, d = calc(i, t, m, d, S, c)
        print(m)
main()
