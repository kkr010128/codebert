H,N=map(int,input().split())

attack = list(map(int,input().split()))

total = sum(attack)

if H - total <= 0:
    print("Yes")
else:
    print("No")