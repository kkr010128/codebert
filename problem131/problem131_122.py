a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
k=abs(a-b)
if 0<=k<=(v-w)*t and v!=w:
    print("YES")
else:
    print("NO")