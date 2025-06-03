N,K = map(int, input().split())
if N % K == 0:
    print(0)
elif N > K:
    hako1 = N%K
    hako2 = abs(hako1-K)
    if hako1 > hako2:
      print(hako2)
    else:
      print(hako1)
else:
    if N >= abs(N-K):
        print(abs(N-K))
    else:
        print(N)