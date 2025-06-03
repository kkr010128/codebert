n = int(input())
a = list(map(int, input().split()))
num = 1
if 0 in a:
    num = 0
else:
    for i in a:
        num *= i
        if 10**18 < num:
            num = -1
            break
print(num)