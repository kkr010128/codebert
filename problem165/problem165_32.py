N = int(input())
C = {}
for _ in range(N):
    s = input().strip()
    if s not in C:
        C[s] = 0
    C[s] += 1
print(len(C))