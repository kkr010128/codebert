N = int(input())
S,T = map(str,input().split())
slist = list(S)
tlist = list(T)
new = ''
for i in range(N):
    new += slist[i]
    new += tlist[i]
print(new)