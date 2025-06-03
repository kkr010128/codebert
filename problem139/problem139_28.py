H1,M1,H2,M2,K=map(int, input().split())

M1 += H1*60
M2 += H2*60
print(M2-M1-K)