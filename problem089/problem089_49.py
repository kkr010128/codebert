h , w , m = map(int,input().split())
retu = [0 for i in range(w)]
gyo = [0 for i in range(h)]
basyo = set()
for i in range(m):
    a , b = map(lambda x:int(x)-1,input().split())
    retu[b] += 1
    gyo[a] += 1
    basyo.add((a,b))
t = max(retu)
mare = [i for i, v in enumerate(retu) if v == t]
s = max(gyo)
magy = [i for i, v in enumerate(gyo) if v == s]

for i in magy:
    for j in mare:
        if not (i,j) in basyo:
            print(s+t)
            exit()
print(s+t-1)