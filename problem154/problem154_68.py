n,k=map(int,input().split())
l =[]
cnt =0
for i in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    for j in a:
        l.append(j)

for i in range(1,n+1):
    if i not in l:
        cnt+=1

print(cnt)