n=int(input())
A=list(map(int,input().split()) )

A.sort()

furui = [0] * (max(A) + 1)

for i in A:
    if furui[i] >= 2:
        continue
    
    for j in range(i,len(furui),i):
        furui[j] += 1

ans=0
for i in A:
    if furui[i]==1:
        ans+=1

print(ans)