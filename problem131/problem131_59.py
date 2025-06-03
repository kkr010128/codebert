a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())

if v<w:
    print("NO")
elif v==w:
    if a==b:
        print("YES")
    else:
        print("NO")
elif v>w:
    t0 = abs((a-b)/(v-w))
    if t0<=t:
        print("YES")
    else:
        print("NO")
