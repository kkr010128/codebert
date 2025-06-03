s = input()
k = len(s)
a = [0]*(k+1)
for i in range(k):
  if s[i] == '<':
    a[i+1] = a[i]+1
for j in range(k-1,-1,-1):
  if s[j] == '>':
    a[j] = max(a[j],a[j+1]+1)
print(sum(a))
