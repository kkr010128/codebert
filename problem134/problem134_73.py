n = int(input())
a = list(map(int,input().split()))
dota = 1
if 0 in set(a):
    dota = 0
else:
    for ai in a:
        dota *= ai
        if dota > 10**18:
            dota = -1
            break
print(dota)