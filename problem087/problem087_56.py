sum = 0
for s in input():
  sum += int(s)
print('Yes' if sum%9==0 else 'No')