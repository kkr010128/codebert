a = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())
for i in range(1, n + 1):
    b, f, r, v = map(int, input().split())
    a[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print("", a[i][j][k], end="")
            if k == 9:
                print()
        if j == 2 and i != 3:
            print("####################")