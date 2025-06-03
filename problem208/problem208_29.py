n, m = map(int, input().split())
dic = {}
flag = True
for _ in range(m):
  digit, num = map(int, input().split())
  if dic.get(digit, None):
    if dic[digit] != num:
      flag = False
      break
  if digit == 1 and num == 0 and n != 1:
    flag = False
    break
  if not dic.get(digit, None):
    dic[digit] = num
if flag:
  lst = [0] * n
  for digit, num in dic.items():
    lst[digit - 1] = num
  s = ''
  if lst[0] == 0 and n != 1:
    lst[0] = 1
  for ele in lst:
    s += str(ele)
  print(int(s))
else:
  print(-1)