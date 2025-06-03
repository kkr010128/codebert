X = int(input())

prime = []
for n in range(3, X, 2):
    lim = int(n ** 0.5)
    f = True
    for p in prime:
        if p > lim:
            break
        if n % p == 0:
            f = False
            break
    if f:
        prime.append(n)
if X >= 3:
    prime = [2] + prime

for n in range(X, X+10**5):
    for p in prime:
        if n % p == 0:
            break
    else:
        print(n)
        break