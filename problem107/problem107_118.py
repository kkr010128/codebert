N = int(input())
X = input()
c = X.count('1')
if c == 0:
  for i in range(N):
    print(1)
  quit()
if c == 1:
  if int(X[-1]):
    for i in range(N-1):
      print(2)
    print(0)
  else:
    for i in range(N-1):
      if int(X[i]):
        print(0)
      else:
        print(1)
    print(2)
  quit()

memo = {0:0, 1:1, 2:1}
def calc(x):
  global memo
  if x in memo:
    return memo[x]
  c = bin(x).count('1')
  y = x % c
  res = calc(y) + 1
  memo[x] = res

for i in range(3, 2*10**5+1):
  calc(i)

Xmodp = Xmodm = 0
digit_p = digit_m = 1
digit = {}
for i in range(N):
  if int(X[-i-1]):
    Xmodp += digit_p
    Xmodp %= c + 1
    Xmodm += digit_m
    Xmodm %= c - 1
  digit[i] = [digit_p, digit_m]
  digit_p = (digit_p * 2) % (c+1)
  digit_m = (digit_m * 2) % (c-1)

ans = []
for i in range(N):
  x = int(X[-i-1])
  if x:
    ans.append(memo[(Xmodm - digit[i][1]) % (c-1)] + 1)
  else:
    ans.append(memo[(Xmodp + digit[i][0]) % (c+1)] + 1)

ans = ans[::-1]
print(*ans, sep='\n')