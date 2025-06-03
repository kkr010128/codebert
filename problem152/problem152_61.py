N = int(input())

memo1 = []
memo2 = []
memo3 = []
memo4 = []
for i in range(N):
  S = input()
  sum_n = sum([1 if s=='(' else -1 for s in S])
  if sum_n >= 0:
    sum_n = 0
    min_n = 1
    for s in S:
      if s == ')':
        sum_n -= 1
        min_n = min(min_n, sum_n)
      else:
        sum_n += 1
    if min_n >= 0:
      memo1.append([min_n, sum_n])
    else:
      memo2.append([min_n, sum_n])
  else:
    sum_n = 0
    min_n = 1
    for s in S[::-1]:
      if s == '(':
        sum_n -= 1
        min_n = min(min_n, sum_n)
      else:
        sum_n += 1
    if min_n >= 0:
      memo4.append([min_n, sum_n])
    else:
      memo3.append([min_n, sum_n])

left = 0
for min_n, sum_n in memo1:
  left += sum_n

memo2.sort(reverse=True)
for min_n, sum_n in memo2:
  if left + min_n < 0:
    print('No')
    quit()
  else:
    left += sum_n

right = 0
for min_n, sum_n in memo4:
  right += sum_n

memo3.sort(reverse=True)
for min_n, sum_n in memo3:
  if right + min_n < 0:
    print('No')
    quit()
  else:
    right += sum_n

if left == right:
  print('Yes')
else:
  print('No')