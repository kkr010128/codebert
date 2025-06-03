n = int(input())
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']

res = ''
while (n > 0):
  n = n - 1
  q = n % 26
  n = n // 26
  res = res + alphabets[q]
res = res[::-1]
print(res)