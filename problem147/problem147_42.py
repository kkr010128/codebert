a = [str(input()) for i in range(2)]
s = a[0]
t = a[1]
s_l = len(s)
S = s + t[s_l]
if S == t:
  print('Yes')
else:
  print('No')