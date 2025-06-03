m = input().split()
K = int(m[0])
X = int(m[1])

ans = 'Yes'

if 500 * K < X:
  ans = 'No'

print(ans)