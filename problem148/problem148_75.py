A, B, C, K = map(int, input().split())
sum = 0
if A > K:
    print(K)
elif A + B > K:
    print(A)
else:
    print(A-(K-A-B))  # =(A+B-(K-(A+B)))