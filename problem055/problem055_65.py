import sys

a=[]
for t in range(4):
    a.append([])
    for f in range(3):
        a[t].append([])
        for r in range(10):
            a[t][f].append(0)

lines = [line for line in sys.stdin]

n = lines[0]

for l in lines[1:]:
    b, f, r, v  = map(int,l.split())
    b -= 1
    f -= 1
    r -= 1
    a[b][f][r] += v

for i,t in enumerate(a):
    for f in t:
        print (" " +" ".join(map(str,f)))
    if len(a) != i +1:
        print ('#'*20)