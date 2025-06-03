#N, K = map(int, input().split( ))
#L = list(map(int, input().split( )))
N = int(input())
i = 0
ans = []
#26^{i}がNを越えるまで以下の操作を繰り返す
while N != 0:
  s = N%26
  if s == 0:
    s = 26
  N -= s
  N //= 26
  ans.append(chr(s + 96))

print(''.join(list(reversed(ans))))