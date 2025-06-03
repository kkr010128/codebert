x = int(input())

num = x // 100
sur = x % 100
if sur <= num * 5:
    print(1)
else:
    print(0)