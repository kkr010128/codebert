s = list(input())
num = 0
n = len(s)
l = 0
i = 0
while i < n:
  if s[i] == '<':
    l+=num
    num+=1
    i+=1
    if i==n:
      l+=num
  else:
    cur = 0
    while i < n and s[i]=='>':
      i+=1
      cur+=1
    if cur <= num:
      l+=num
      cur-=1
    l+=(cur*(cur+1))//2
    num = 0
print(l)