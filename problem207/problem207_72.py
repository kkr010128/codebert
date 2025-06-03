import sys

a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]

card = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if(b[i] == a[j][k]):
                card[j][k] = 1

if card[0].count(1) == 3:
    print("Yes")
    sys.exit()

if card[1].count(1) == 3:
    print("Yes")
    sys.exit()

if card[2].count(1) == 3:
    print("Yes")
    sys.exit()

if card[0][0] == 1 and card[1][0] == 1 and card[2][0] == 1:
    print("Yes")
    sys.exit()

if card[0][1] == 1 and card[1][1] == 1 and card[2][1] == 1:
    print("Yes")
    sys.exit()

if card[0][2] == 1 and card[1][2] == 1 and card[2][2] == 1:
    print("Yes")
    sys.exit()

if card[0][0] == 1 and card[1][1] == 1 and card[2][2] == 1:
    print("Yes")
    sys.exit()

if card[0][2] == 1 and card[1][1] == 1 and card[2][0] == 1:
    print("Yes")
    sys.exit()

print("No")
