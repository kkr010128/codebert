n, s = open(0).read().split()

s = list(map(int, list(s)))

from itertools import product,repeat

ans = 0
for a,b,c in product(range(10), range(10), range(10)):
    abc = [a,b,c]
    tmp = 0
    for dig in s:
        if dig == abc[tmp]:
            tmp += 1
            if tmp == 3:
                ans += 1
                break

print(ans)