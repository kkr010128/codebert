from collections import Counter
n = int(input())
a = list(map(int,input().split()))

ja1 = []
ja2 = []
for i in range(1,n+1):
  ja1.append(i-a[i-1])
  ja2.append(i+a[i-1])

s = Counter(ja1)
t = Counter(ja2)

su = 0
for i in s.keys():
  su += s[i]*t[i]
print(su)