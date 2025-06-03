N = int(input())

x = 0
for i in range(N):
    a, b = map(int, input().split())
    if a == b:
        x += 1
    else:
        x = 0

    if x >= 3:
        print("Yes")
        break
else:
    print("No") 