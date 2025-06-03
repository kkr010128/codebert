import sys

N = int(sys.stdin.readline())
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            print("Yes")
            sys.exit()

print("No")