N = int(input())
n = min(N, 10**6)
is_Prime = [True] * (n + 1)
is_Prime[0] = False
is_Prime[1] = False
for i in range(2, int(n**(1/2)+1)):
    for j in range(2*i, n+1, i):
        if j % i == 0:
            is_Prime[j] = False
P = [i for i in range(n+1) if is_Prime[i]]

count = 0
for p in P:
    count_p = 0
    while N % p == 0:
        count_p += 1
        N /= p
    count += int((-1+(1+8*count_p)**(1/2))/2)
    if p == P[-1] and N != 1:
        count += 1
print(count)