N,A,B = map(int,input().split())
i = N // (A + B)
N -= (A + B) * i

cnt_A = i * A

if N < A:
  cnt_A += N
else:
  cnt_A += A
  
print(cnt_A)