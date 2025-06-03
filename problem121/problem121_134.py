alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = int(input())

str = ''
count = 0
while True:
  n -= 26 ** count
  if n < 26 ** (count + 1):
    while count != 0:
      mod = 26 ** count
      num_1 = n // mod
      n %= mod
      str = str + alph[num_1]
      count -= 1
    break
  count += 1
str = str + alph[n]
print(str)