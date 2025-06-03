n, k = map(int, input().split())
P = list(map(int, input().split()))

P_ac = [sum(P[:k])]
for i in range(n-k):
    P_ac.append(P_ac[-1]-P[i]+P[i+k])

print((max(P_ac)+k)/2)