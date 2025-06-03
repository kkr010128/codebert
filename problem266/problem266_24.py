x = int(input())
a = x//100
b = x%100
l = list(range(1,6))[::-1]
i = 0
cnt = 0
while b > 0:
  if l[i] > b: i += 1
  cnt += b//l[i]
  b = b % l[i]
print(1 if cnt <= a else 0)