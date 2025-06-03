s = input()
a = [str(c) for c in s]
t = input()
b = [str(c) for c in t]

c = 0
n = len(a)
for i in range(n):
  if a[i] == b[i]:
    c +=1

print(n-c)
