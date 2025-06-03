import sys

n = int(input())

for i in range(int(n / 1.08), int(n / 1.08) + 2):
    if int(i * 1.08) == n:
        print(i)
        sys.exit()
else:
    print(":(")
