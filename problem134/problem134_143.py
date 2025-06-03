n = int(input())
lst = sorted(list(map(int, input().split())))
mult = 1

for i in lst:
    mult *= i
    if 10**18 < mult:
        print(-1)
        exit()
else:
    print(mult)