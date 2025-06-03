A, V =map(int, input().split())
B, W =map(int, input().split())
T=int(input())

d=abs(B-A)
dv=V-W

if dv<=0:
    print("NO")

elif d/dv > T:
    print("NO")
else:
    print("YES")