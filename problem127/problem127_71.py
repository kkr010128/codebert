X,Y = map(int,input().split())
ans = False

for t in range(101):
    for k in range(101):
        if t+k == X and 2*t + 4*k == Y:
            ans = True

if ans:
    print("Yes")
else:
    print("No")