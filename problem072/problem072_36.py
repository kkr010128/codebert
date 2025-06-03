n = int(input())

ans = 0
flag = 0

for i in range(0, n):
    x, y = input().split()
    if x == y:
        ans = ans + 1
    else:
        ans = 0
    if ans >= 3:
        flag = 1
if flag == 1:
    print("Yes")
else :
    print("No")
