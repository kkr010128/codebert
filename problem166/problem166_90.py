s = input()[::-1]
counts = [0] * 2019
counts[0] = 1
digit = 1
sum = 0
for c in s:
  sum = (sum + int(c) * digit) % 2019
  digit = digit * 10 % 2019
  counts[sum] += 1
 
result = 0
for c in counts:
  result += c * (c - 1) // 2
 
print(result)