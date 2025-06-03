H1,M1,H2,M2,K = map(int,input().split())
start,end = 60*H1+M1,60*H2+M2
print(abs(start-end) - K) if end-K>0 else print(0)