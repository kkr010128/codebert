from itertools import permutations

N=int(input())
ans = ['']*N

al = 'abcdefghij'
d = {al[i]:i for i in range(N)}

def dfs(h=[]):
    if len(h)==N:
        print(''.join(h))
        return
    for i in range(max([d[h[-1-i]] for i in range(len(h))])+2):
        h.append(al[i])
        dfs(h)
        h.pop()
    return
  
dfs(['a'])