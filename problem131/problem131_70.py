a, v=map(int, input().split())
b, w=map(int, input().split())
t=int(input())

distance=abs(a-b)
speed=v-w

if speed<=0:
    print("NO")
else:
    if distance/speed <=t:
        print("YES")
    else:
        print("NO")