N = int(input())
l = []
for i in range(N):
    l.append([int(x) for x in input().split()])

xlim = []
ylim = []

def cha(a):
    return [a[0]-a[1],a[0]+a[1]]

for i in range(N):
        ylim.append(cha(l[i])[1])
        xlim.append(cha(l[i])[0])

xlim.sort()
ylim.sort()

print(max(xlim[-1]-xlim[0],ylim[-1]-ylim[0]))