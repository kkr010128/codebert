H1,M1,H2,M2,K = map(int,input().split())
A1 = H1*60+M1
A2 = H2*60+M2
print(max(0,A2-A1-K))