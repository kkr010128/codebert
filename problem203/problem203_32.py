A, B = [int(i) for i in input().split()]
# たかだか1250円
for i in range(1300):
    a = (i * 8) // 100
    b = i //10
    if A == a and B == b:
        print(i)
        exit()
print(-1)