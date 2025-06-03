x, y = map(int, input().split())
for a in range(x+1):
    for b in range(x+1-a):
        if a + b == x and 2*a + 4*b == y:
            print("Yes")
            exit()
print("No")