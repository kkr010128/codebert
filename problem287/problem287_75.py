n = int(input())
x = 0
for i in range(1, 10):
    if n % i == 0 and n / i < 10:
        x += 1
        break
    else:
        pass
if x == 1:
    print('Yes')
else:
    print('No')