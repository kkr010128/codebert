N = input()

sum = 0

for i in range(10):
    sum += N.count(str(i)) * i

print('Yes' if sum%9 == 0 else 'No')