a,b=map(int, input().split())
c=list(map(int, input().split()))
l =[]
ans = 0

def abc(n):
    return (n+1)/2

cb = list(map(abc,c))

s = sum(cb[:b])
l.append(s)

for i in range(b,a):
    s = s - cb[i-b] + cb[i]
    l.append(s)

L = sorted(l)
print(L[-1])