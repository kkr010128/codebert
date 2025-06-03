A,B,K = map(int,input().split())

C = max(0,A+B-K)

B2 = min(C,B)
A2 = C-B2
print(A2,B2)