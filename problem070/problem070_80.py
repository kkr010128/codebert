import math

n, M= map(int,input().split())
#AB=[]
#N = int(input())
#C = input()
parents = [-1] * n

def find( x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x, y = y, x

    parents[x] += parents[y]
    parents[y] = x

def size( x):
    return -parents[find(x)]

def same( x, y):
    return find(x) == find(y)

def members( x):
    root = find(x)
    return [i for i in range(n) if find(i) == root]

def roots():
    return [i for i, x in enumerate(parents) if x < 0]

def group_count():
    return len(roots())

def all_group_members():
    return {r: members(r) for r in roots()}

def __str__():
    return '\n'.join('{}: {}'.format(r, members(r)) for r in roots())
 
C = []
for i in range(M):
    A, B = map(int,input().split())
    union(A-1,B-1)
    '''
    c = 0
    for p in C:
        if A in p:
            c = 1
            p.add(B)
        elif B in p:
            c = 1
            p.add(A)
    if c != 1:
        C.append(set([A,B]))
    '''
print(group_count()-1)
