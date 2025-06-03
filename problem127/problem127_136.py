
X, Y = map(int, input().split())

for k in range(X+1):
    t = X - k
    if k*4 + t*2 == Y:
        print("Yes")
        exit()
print("No")
