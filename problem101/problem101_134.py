A, B, C = map(int, input().split())
K = int(input())
while A >= B and K > 0:
    B *= 2
    K -= 1
while B >= C and K > 0:
    C *= 2
    K -= 1
# print(A, B, C, K)
if A < B and B < C:
    print("Yes")
else:
    print("No")
