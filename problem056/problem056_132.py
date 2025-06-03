n, m = map(int, input().split(' '))
A = []
i = 0
while i < n:
    a = list(map(int, input().split(' ')))
    A.append(a)
    i += 1
x = []
j = 0
while j < m:
    x.append(int(input()))
    j += 1
ans = ''
p = 0
while p < n:
    q = 0
    a0 = 0
    while q < m:
        a0 += A[p][q] * x[q]
        q += 1
    ans += str(int(a0)) + '\n'
    p += 1
print(ans[:-1])
