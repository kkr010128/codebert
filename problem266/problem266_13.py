X=int(input())
#m1,d1=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

flag=0
for i in range(1,1001):
    if i*100 <= X and X <= i*105:
        flag=1
        break
print(flag)
