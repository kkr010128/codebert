D = int(input())
c = list(map(int, input().split()))
s_matrix = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) for _ in range(D)]
last = [0] * 26
satis = 0

for i in range(D):
    test = t[i] - 1
    satis += s_matrix[i][test]
    last[test] = i + 1
    for j in range(26):
        satis -= c[j] * (i+1 - last[j])
    print(satis)
