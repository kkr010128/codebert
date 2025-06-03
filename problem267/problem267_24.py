from collections import defaultdict

N=int(input())
S=input()

d = defaultdict(list)
for i in range(N):
  d[int(S[i])].append(i)
    
ans = 0
for n1 in range(10):
  if not d[n1]:continue
  for n2 in range(10):
    if not d[n2]:continue
    if d[n1][0]>d[n2][-1]: continue
    for n3 in range(10):
      if not d[n3]:continue
      if d[n1][0]>d[n3][-1] or d[n2][0]>d[n3][-1]:continue
      for idx in d[n2]:
        if idx>d[n1][0] and idx<d[n3][-1]:
          ans += 1
          break
            
print(ans)