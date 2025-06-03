N = int(input())
x = []
hp = []
xa = 0
hpsum = 0

x = [int(e) for e in input().split()]
for i in range(N):
    xa += x[i]



xa = xa / N

if xa % 1 < 0.5:
    xa = int(xa / 1)
elif xa % 1 >= 0.5:
    xa = int(xa / 1 + 1)

for j in range(N):
    hp.append((x[j]-xa)*(x[j]-xa))
    hpsum += hp[j]

print(int(hpsum))