n,k,c = list(map(int, input().split()))
s = list(input())
l = []
r = []

i = 0
while i < n and len(l) <= k:
  if s[i] == "o":
    l.append(i)
    i += (c + 1)
  else:
    i += 1

i = n-1
while i >= 0 and len(r) <= k:
  if s[i] == "o":
    r.append(i)
    i -= (c+1)
  else:
    i -= 1
  
i = 0
while i < k:
  if l[i] == r[k-1-i]:
    print(l[i]+1)
  i += 1
  
  

