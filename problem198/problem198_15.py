n = int(input())

alphabets = [chr(ord('a') + x) for x in range(26)]

tmp = []

def dfs(s, i):
    if len(s) == n:
        yield s
        return
    for j in range(i):
        for k in dfs(s+alphabets[j], i):
            yield k
    for k in dfs(s+alphabets[i], i+1):
        yield k

for w in dfs('', 0):
    print(w)