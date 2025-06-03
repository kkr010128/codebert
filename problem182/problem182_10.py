N, K, C = map(int, input().split())
S = input()

must = set()
i = len(S)+C
for j in range(K):
  i = S.rindex("o", 0, i-C)
  must.add(i)
if i<=C or "o" not in S[:i-C]:
  i = -C-1
  for j in range(K):
    i = S.index("o", i+C+1)
    if i in must:
      print(i+1)