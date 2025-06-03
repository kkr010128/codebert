n = int(input())
p = []
q = []
r = []
for i in range(2,(int(n**0.5)+1)):
    N = n
    if N%i == 0:
        p.append(i)
for i in range(2,(int(n**0.5)+1)):
    N = n - 1
    if N%i == 0:
        r.append(i)
        if i != N//i:
            r.append(N//i)
for i in range(len(p)):
    N = n
    while N % p[i] == 0:
        N = N / p[i]
    if N % p[i] == 1:
        q.append(p[i])
for i in range(len(r)):
    if n % r[i] == 1:
        q.append(r[i])
if n == 2:
    print(1)
else:
    print(len(q)+2)