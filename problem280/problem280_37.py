import itertools

N = int(input())
l = []
kyori = []

for _ in range(N):
    xy = list(map(int, input().split()))
    l.append(xy)

for i in itertools.combinations(l,2):
    t = ((i[0][0]-i[1][0])**2 + (i[0][1] - i[1][1])**2)**0.5
    kyori.append(t)

print((N-1)*sum(kyori)/len(kyori))