S = input()
acc = 0
for ch in S:
  acc += int(ch)
print('Yes' if acc % 9 == 0 else 'No')