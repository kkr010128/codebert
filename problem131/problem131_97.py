a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
d=abs(a-b)
if v<=w:
    print("NO")
    exit()
if d<=t*(v-w):
    print("YES")
else:
    print("NO")