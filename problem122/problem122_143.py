N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = [0]*Q
C = [0]*Q
for i in range(Q):
    B[i], C[i] = map(int,input().split())
    
num = [0]*100001
for i in A:
    num[i] += 1

S = [0]*(Q+1)
S[0] = sum(A)
change = 0
for i in range(Q):
    change = num[B[i]]
    S[i+1] = S[i] + change*(C[i]-B[i])
    num[B[i]] -= change
    num[C[i]] += change
    
for i in S[1:]:
    print(i)