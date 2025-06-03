a = [input().split() for l in range(3)]
n = int(input())
b = list(input() for i in range(n))
c = [[0] * 3 for i in range(3)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if b[i] == a[j][k]:
                c[j][k] = 1

if (c[0][0] == 1 and c[0][1] == 1 and c[0][2] == 1) or(c[1][0] == 1 and c[1][1] == 1 and c[1][2] == 1) or(c[2][0] == 1 and c[2][1] == 1 and c[2][2] == 1) or(c[0][0] == 1 and c[1][0] == 1 and c[2][0] == 1) or(c[0][1] == 1 and c[1][1] == 1 and c[2][1] == 1) or(c[0][2] == 1 and c[1][2] == 1 and c[2][2] == 1) or(c[0][0] == 1 and c[1][1] == 1 and c[2][2] == 1) or (c[0][2] == 1 and c[1][1] == 1 and c[2][0] == 1):
    print("Yes")
else:
    print("No")
