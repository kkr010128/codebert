N = int(input())
s, t = map(str, input().split())
ans = []
for i in range(N):
  a = s[i] + t[i]
  ans.append(a)
print(''.join(ans))