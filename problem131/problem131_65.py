a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
if a > b:
    oni = a + (-1*v) * t
    nige = b + (-1*w) * t
    if oni <= nige:
        print("YES")
    else:
        print("NO")
else:
    oni = a + v*t
    nige = b + w * t
    if oni >= nige:
        print("YES")
    else:
        print("NO")