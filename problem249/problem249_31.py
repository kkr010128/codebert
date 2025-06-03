A,B,K = map(int,input().split())
if A+B < K:
    print(0,0)
    exit()
elif A - K < 0:
    B = B + A - K 
    A = 0
elif A - K >= 0:
    A = A - K
print(A,B)