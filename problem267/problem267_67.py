N = int(input())
S = list(input())
S = list(map(lambda x: int(x), S))

ans = 0

for i in range(10):
  for j in range(10):
    for k in range(10):
      if i in S:
        a = S.index(i)
        if j in S[a+1:]:
          b = S[a+1:].index(j) + a + 1
          if k in S[b+1:]:
            ans += 1
          else:
            continue
        else:
          continue
      else:
        continue

print(ans)
