import sys
N,A,B = map(int,input().split())

if not ( 1 <= N <= 10**18 and 0 <= A and 0 <= B and 0 < A + B <= 10**18 ): sys.exit()
if not ( isinstance(N,int) and isinstance(A,int) and isinstance(B,int) ): sys.exit()

count = N // (A+B)
remind = N % (A+B) if N % (A+B) <= A else A
    
print(count * A + remind)