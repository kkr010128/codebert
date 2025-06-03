N, K, C = map(int,input().split())
S = list(input())

def solve(List):
    ans = []
    i = 0
    while i < N:
        if List[i] == 'o':
            ans.append(i+1)
            i += C
        i += 1
    return ans

n = solve(S)

if len(n) > K:
    pass
else:
    r = solve(S[::-1])
    r = list(map(lambda x: N+1-x, r[::-1]))
    ans = list(set(n) & set(r))
    ans.sort()
    for i in ans:
        print(i)