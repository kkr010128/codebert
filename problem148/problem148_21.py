# Easy Liniear Programming
A,B,C,K = map(int,input().split())
ans = min(A,K)*1 + max(0, K-A)*0 + max(0, K-A-B)*(-1)
print(ans)