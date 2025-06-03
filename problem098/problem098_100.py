n = int(input())
s = input()
nr = s.count('R')
nw = len(s)-nr
a = ('R'*nr)+('W'*nw)
c = 0
for i in range(n):
  if(s[i:i+1] != a[i:i+1]):
    c += 1
print(c // 2)