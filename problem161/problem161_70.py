A,B,N = list(map(int, input().split()))

#floor(A*x // B vs A * (x/B)
#x= pB + q (0<=q<B)
# Ap +(Aq// B)  - AP
x = B-1 if B<=N else N
print((A*x) // B)