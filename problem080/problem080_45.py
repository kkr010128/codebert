n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    z = a + b
    w = a - b
    A.append(z)
    B.append(w)
    
P = abs(max(A) - min(A))
Q = abs(max(B) - min(B))
print(max(P, Q))