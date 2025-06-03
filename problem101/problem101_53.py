A, B, C  = map(int, input().split())
K = int(input())
flg = 0
for i in range(K):
  if B > A:
    if C > B or 2*C > B:
      flg = 1
    else:
        C = 2*C
  else:
    B = 2*B
    continue
if flg:
    print('Yes')
else:
    print('No')