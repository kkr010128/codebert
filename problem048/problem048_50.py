n = input()
l = map(int, raw_input().split())
max = l[0]
min = l[0]
s = 0
for i in range(n):
 if max < l[i]:
  max = l[i]
 if min > l[i]:
  min = l[i]
 s = s + l[i]
print min, max, s