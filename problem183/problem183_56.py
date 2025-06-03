N = int(input())
if N == 2:
    print(1)
    exit()
ans = 1
divisors = []
d = 2
while d*d < N:
    if N % d == 0:
        divisors.append(d)
        divisors.append(N//d)
    d += 1
if d*d == N:
    divisors.append(d)

for d in divisors:
    dummyN = N
    while dummyN % d == 0:
        dummyN //= d
    if dummyN % d == 1:
        ans += 1

N -= 1
divisors = []
d = 2
while d*d < N:
    if N % d == 0:
        divisors.append(d)
        divisors.append(N//d)
    d += 1
if d*d == N:
    divisors.append(d)

ans += len(divisors)+1
print(ans)