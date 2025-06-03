n = int(input())

for i in range(2, n + 1):
  if i % 3 == 0 or i % 10 == 3 or '3' in str(i // 10):
    print('', i, end = '')
print()
