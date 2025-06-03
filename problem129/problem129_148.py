# Not Divisible

N = int(input())
A = [int(n) for n in input().split()]

check = [0] * 1000001
A.sort()

ok = [-1]
p = 0
for a in A:
    if a == p:
        if ok[-1] == p:
            ok = ok[:-1]
        continue
    p = a
    if check[a] == 1:
        continue
    for i in range(a, 1000001, a):
        check[i] = 1
    ok.append(a)

print(len(ok) - 1)
