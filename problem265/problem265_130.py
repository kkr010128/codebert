n = int(input())
for i in range(100000):
    if i * 108 // 100 == n:
        print(i)
        break
else:
    print(':(')