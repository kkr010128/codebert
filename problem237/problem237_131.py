from operator import itemgetter

n=int(input())
XL=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    XL[i].append(XL[i][0]+XL[i][1])

XL.sort(key=itemgetter(2))

cnt=1
choice=0

for i in range(n):
    if XL[choice][2]<=XL[i][0]-XL[i][1]:
        choice=i
        cnt+=1

print(cnt)