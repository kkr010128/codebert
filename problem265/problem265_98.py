n = int(input())
x = int(n / 1.08)

if int(x * 1.08) == n:
    print(x)
elif int((x-1) * 1.08) == n:
    print(x-1)
elif int((x+1) * 1.08) == n:
    print(x+1)
else:
    print(':(')