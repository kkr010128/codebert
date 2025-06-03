H1, M1, H2, M2, K = map(int, input().split())

x = H1*60+M1
y = H2*60+M2

print(y-x-K)