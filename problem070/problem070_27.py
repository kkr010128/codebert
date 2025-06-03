N, M = map(int, input().split())
parents = [i for i in range(N+1)]

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
    
def same(A, B):
    x, y = find(A), find(B)
    if x==y:
        return
    else:
        parents[x] = y

for _ in range(M):
    A, B = map(int, input().split())
    same(A, B)
    
for i in range(N):
    find(i+1)

print(len(set(parents)) - 2)