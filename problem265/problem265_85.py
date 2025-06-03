n = int(input())

if n/1.08==n//1.08:
    print(n//1.08)
elif int(-(-n//1.08) * 1.08) == n:
    print(int(-(-n//1.08)))
else:
    print(':(')