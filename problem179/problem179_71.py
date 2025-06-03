n,m = map(int,input().split())
alist = list(map(int,input().split()))

alist.sort(reverse=True)
allvote = sum(alist)

count = 0
for i in range(n):
    if alist[i] >= allvote/(4*m):
        count+=1

if count >= m:
    print("Yes")
else:
    print("No")