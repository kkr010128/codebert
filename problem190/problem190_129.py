S = input()
n = len(S)
confS = S[::-1]
flag1 = False
flag2 = False
flag3 = False
s1 = S[0:int((n-1)/2)]
confs1 = s1[::--1]
s2 = S[int((n+3)/2)-1:n]
confs2 = s2[::-1]
if S == confS:
  flag1 = True
if s1 == confs1:
  flag2 = True
if s2 == confs2:
  flag3 = True
if flag1 and flag2 and flag3:
  print("Yes")
else:
  print("No")