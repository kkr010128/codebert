import itertools

a = []
while True:
    d = list(map(int,input().split()))
    if d == [0,0]:
        break
    a.append(d)

for n,x in a:
    ans = 0
    for c in itertools.combinations(range(1,n+1), 3):
        if sum(c) == x: ans += 1
    print(ans)