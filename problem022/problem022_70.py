N = int(input())
S = [int(x) for x in input().split()]
T = int(input())
Q = [int(x) for x in input().split()]

c = 0

def seach(A, n, key):
    i = 0
    A = A + [key]
    while A[i] != key:
        i += 1
    return i != n

for q in Q:
    if seach(S, N, q):
        c += 1
        
print(c)
