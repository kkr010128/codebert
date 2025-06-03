s = list(input())
num = 0
n = len(s)
l = []
i = 0
while i < n:
  if s[i] == '<':
    l.append(num)
    num+=1
    i+=1
    if i==n:
      l.append(num)
  else:
    cur = 0
    while i < n and s[i]=='>':
      i+=1
      cur+=1
    if cur <= num:
      l.append(num)
      cur-=1
    l.append((cur*(cur+1))//2)
    num = 0
print(sum(l))