import sys
A,B,K = map(int,input().split())

if not ( 0 <= A <= 10**12 and 0 <= B <= 10**12 and 0 <= K <= 10**12 ): sys.exit()
if not ( isinstance(A,int) and isinstance(B,int) and isinstance(K,int) ): sys.exit()

if K >= A:
    if (K - A) >= B:
        B = 0
    elif (K - A) < B:
        B = B - (K - A)
    A = 0
elif K < A:
    A = A - K
print(A,B)