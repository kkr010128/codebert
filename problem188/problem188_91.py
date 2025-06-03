x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

ans = 0
p.sort(reverse = True)
q.sort(reverse = True)
r.sort(reverse = True)
p = p[:x]
q = q[:y]

P = sum(i for i in p)
Q = sum(j for j in q)
ans = P+Q
apples = p+q
apples.sort()
for i in range(len(r)):
  if apples[i] < r[0]:
    ans = ans-apples[i] + r[0]
    del r[0]
  else:
    break
print(ans)