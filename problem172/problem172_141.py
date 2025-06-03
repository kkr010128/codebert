o = ['No','Yes']
f = 0
N = input()
s = str(N)
for c in s:
    t    = int(c)
    if t == 7:
        f = 1
print(o[f])