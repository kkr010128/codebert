s = list(input())
t = list(input())
cnt = 0
for (s1,t1) in zip(s,t):
  if s1 != t1:
    cnt += 1
print(cnt)