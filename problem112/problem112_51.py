
INF = 10 ** 9 + 7
N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

if K == 1:
    print(a[0])
    exit()

if K == N:
    ans = 1
    for i in a:
        ans *= i
        ans %= INF
    print(ans)
    exit()

if a[0] < 0:
    ans = 1
    if K % 2 == 1:
        for i in range(K):
            ans *= a[i]
            ans %= INF
    else:
        for i in range(K):
            ans *= a[-i - 1]
            ans %= INF
    print(ans)
    exit()

sei = []
hu = []
for i in a:
    if i >= 0:
        sei.append(i)
    else:
        hu.append(i)
hu.sort()
seis = []
hus = []
total = []
ans = 1

if K % 2 != 0:
    ans = sei[0] % INF
    for i in range(2, len(sei), 2):
        seis.append(sei[i] * sei[i - 1])
else:
    for i in range(1, len(sei), 2):
        seis.append(sei[i] * sei[i - 1])
for i in range(1, len(hu), 2):
    hus.append(hu[i] * hu[i - 1])

total = hus + seis
total.sort(reverse=True)
for i in range(K // 2):
    ans *= total[i]
    ans %= INF

print(ans)
