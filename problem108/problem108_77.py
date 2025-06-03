i = int(input().strip())
if i % 1000 == 0:
    print('0')
else:
    print((i // 1000 + 1) * 1000 - i)
