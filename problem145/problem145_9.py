from collections import deque
n,m = map(int, input().split())
ikisaki=[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    ikisaki[a].append(b)
    ikisaki[b].append(a)
ans=[0]+[1]+[0]*(n-1)
tansakuheya=deque([1])
tmp=deque()

for _ in range(1000009):

    for bangou in tansakuheya:

        for heya in ikisaki[bangou]:
            if ans[heya]==0:
                ans[heya]=bangou
                tmp.append(heya)

    tansakuheya=tmp.copy()
    tmp=deque()


    if not tansakuheya:
        break

print("Yes")
for i in range(2,n+1):
	print(ans[i])