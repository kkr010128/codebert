n=int(input())

s = ''
for i in range(11):
  if n != 0:
    n -= 1
    s += chr(ord('a') + n % 26)
    n //= 26
print(s[::-1])