H1, M1, H2, M2, K = list(map(int,input().split()))
a = 60*H1 + M1
b = 60*H2 + M2
print(b - a - K)