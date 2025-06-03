A,V=map(int, input().split())
B,W=map(int, input().split())
T=int(input())

if W>=V:
    print("NO")
    quit()

SA=abs(A-B)

IDOU=V-W

IDOUTARN=IDOU*T

ANS=SA-IDOUTARN

if ANS<=0:
    print("YES")
else:
    print("NO")