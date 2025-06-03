H1, M1, H2, M2, K = map(int, input().split())
s = H1*60 + M1
e = H2*60 + M2
print(e - K - s)