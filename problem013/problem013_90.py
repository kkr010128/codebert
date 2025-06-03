dif = -1E9
n = int(input())
mn = int(input())
for i in range(n - 1):
    r = int(input())
    if r - mn > dif:
        dif = r - mn
    if r < mn:
        mn = r
print(dif)