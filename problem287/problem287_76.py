import sys
input = sys.stdin.readline

n = int(input())

flag = False

for i in range(1, 10):
    if n % i == 0 and 1 <= n // i <= 9:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")

