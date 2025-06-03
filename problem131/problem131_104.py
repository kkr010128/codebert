
l=list(map(int, input().split(' ')))
a=l[0]
v=l[1]
l=list(map(int, input().split(' ')))
b=l[0]
w=l[1]
s=int(input())
ans=True
if a>b:
    ans=a-v*s<=b-w*s
else:
    ans=a+v*s>=b+w*s
if ans:
    print("YES")
else:
    print("NO")
    

