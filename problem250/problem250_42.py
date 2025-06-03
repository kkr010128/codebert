X = int(input())

n = 10**6
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * 2, n + 1, i):
        is_prime[j] = False

for i, p in enumerate(is_prime):
    if i >= X and p is True:
        print(i)
        break