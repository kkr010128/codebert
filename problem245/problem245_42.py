n = int(input())
s = str(input())
count = 0
if n % 3 == 1 or n % 3 == 0:
  for i in range(n-1):
    if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
      count += 1
elif n % 3 == 2:
  for i in range(n-2):
    if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
      count += 1
print(count)
