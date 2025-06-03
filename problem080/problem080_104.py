N = int(input())
xys = set([tuple(map(int, input().split())) for _ in range(N)])

z = []
w = []

for xy in xys:
    z.append(xy[0]+xy[1])
    w.append(xy[0]-xy[1])

#print(z)
#print(w)

print(max(abs(max(z) - min(z)), abs(max(w) - min(w))))