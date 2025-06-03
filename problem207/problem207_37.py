a = []
for i in range(3):
    a.append(list(map(int, input().split())))
n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k] == b:
                a[j][k] = 0

for i in range(3):
    if sum(a[i]) == 0:
        print("Yes")
        exit()
for i in range(3):
    if sum([a[0][i], a[1][i], a[2][i]]) == 0:
        print("Yes")
        exit()
if sum([a[0][0], a[1][1], a[2][2]]) == 0 or sum([a[0][2], a[1][1], a[2][0]]) == 0:
    print("Yes")
    exit()
print("No")