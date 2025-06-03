n = int(input())
s = input()
if n % 2 == 1:
  print('No')
  exit()
n2 = n // 2
for i in range(n2):
  if s[i] != s[i+n2]:
    print('No')
    exit()
print('Yes')