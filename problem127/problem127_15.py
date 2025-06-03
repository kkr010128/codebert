X,Y = map(int,input().split())
for i in range(X+1):
    a = i*2 + (X-i)*4
    if a == Y:
        print("Yes")
        break
if a != Y:
    print("No")
