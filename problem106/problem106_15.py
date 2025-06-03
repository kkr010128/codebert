n = int(input())

ANS = [0] * (n+1)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            tmp = (x + y + z)**2 - z*(x + y) - (x*y)
            if tmp > n: continue
            ANS[tmp] += 1

for ans in ANS[1:]:
    print(ans)