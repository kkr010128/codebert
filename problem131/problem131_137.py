a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
if v <= w:
    print("NO")
else:
    dis = abs(b-a)
    sp = abs(v-w)
    if 0 < dis/sp <= t:
        print("YES")
    else:
        print("NO")
