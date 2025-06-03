import sys
N = input()
num = [int(x) for x in input().split()]
multiply = 1

if (0 in num):
    print(0)
    sys.exit()

for i in num:
    multiply *= i
    if (multiply > 10**18):
        print(-1)
        sys.exit()
if (0 < multiply and multiply <= 10**18):
    print(multiply)