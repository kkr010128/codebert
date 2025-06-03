n = int(input())

moziretu={}
a=1
for i in range(n):
    s=input()

    if s in moziretu:
        moziretu[s]=moziretu[s]+1
        a=max(a,moziretu[s])
    else:
        moziretu[s]=1

ans=[k for k, v in moziretu.items() if v == a]
ans.sort()
for i in ans:
    print(i)