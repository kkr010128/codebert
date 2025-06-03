n = int(input())

digit = 1
while n > 26 ** digit:
  n -= 26 ** digit
  digit += 1

ans = []
n -= 1
char = 'abcdefghijklmnopqrstuvwxyz'
for i in list(range(digit)):
  ans.append(char[n % 26])
  n -= n%26
  n = int(n/26)

print(''.join(reversed(ans)))