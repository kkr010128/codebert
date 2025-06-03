cnt = 0
n = int(input())
l = list(map(int, input().split()))
if len(l) >= 3:
  for i in range(len(l)):
    for j in range(i, len(l)):
      for k in range(j, len(l)):
        if l[i] == l[j] or l[i] == l[k] or l[j] == l[k]:
          continue
        elif l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]:
          cnt += 1
        else:
          continue
print(cnt) 