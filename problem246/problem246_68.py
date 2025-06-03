import itertools

n = int(input())
j = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
j_i, q_i = None, None
for i, t in enumerate(itertools.permutations(range(1,n+1), n), start=1):
    if t == j:
        j_i = i
    if t == q:
        q_i = i
    if j_i and q_i:
        break
print(abs(j_i - q_i))
