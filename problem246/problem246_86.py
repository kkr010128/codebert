from itertools import permutations

def same(l1, l2, n):
    for i in range(n):
        if l1[i] != l2[i]:
            return False
    return True

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

P = [p-1 for p in P]
Q = [q-1 for q in Q]

for i,pattern in enumerate(permutations(range(N))):
    if same(P, pattern, N):
        i_p = i
    if same(Q, pattern, N):
        i_q = i

print(abs(i_p - i_q))