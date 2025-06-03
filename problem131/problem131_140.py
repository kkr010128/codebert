a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
#a,b間の距離
d=abs(b-a)
#速度差
V=v-w
if V<=0:
    print("NO")
    exit()
T=d/V
if T<=t:
    print("YES")
else:
    print("NO")