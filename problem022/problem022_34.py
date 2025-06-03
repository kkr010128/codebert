N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))
C = 0
for i in range(Q):
    if T[i] in S:
        C+=1
print(C)
