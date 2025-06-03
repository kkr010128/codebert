n = int(input())
x = input()
a = x.count('1')
b = int(x,2)
# print (b)

ary = [None for i in range(200010)]
ary[0] = 0

def f(n):
  if ary[n] is not None:
    return ary[n]
  b = bin(n).count('1')
  r = 1 + f(n%b)
  ary[n] = r
  return ary[n]


a1 = a + 1
a0 = a - 1
for i in range(200010):
  f(i)


one = [1] * 200010
zero = [1] * 200010
for i in range(1, 200010):
    if a0 != 0:
        one[i] = one[i-1] * 2 % a0
    zero[i] = zero[i-1] * 2 % a1


ans = [0 for i in range(n)]
c1 = b%a1
if a0 != 0:
  c0 = b%a0
for i in range(n-1, -1, -1):
  if x[n-1-i] == '0':
    y = c1 + zero[i]
    # y = x %a1
    y %= a1
    print (ary[y]+1)
  else:
    if a0 != 0:
      y = c0 - one[i]
      y %= a0
      print (ary[y]+1)
    else:
      print (0)
# ans.reverse()
# for i in ans:
#   print (i)