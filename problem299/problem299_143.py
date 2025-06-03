N = int(input())
alist = list(map(int, input().split()))
blist = []
for i in range(N):
    blist.append([alist[i],i+1])
blist.sort()
for i in range(N):
    print(blist[i][1],end=" ")