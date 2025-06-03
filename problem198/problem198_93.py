n = int(input())
alp = [chr(ord("a") + x) for x in range(26)]

def dfs(S):
    if len(S) == n:
        print(S)
    else:
        max_s = ord(max(S)) - 96
        #print(max_s)
        for i in range(max_s + 1):
            dfs(S + alp[i])

dfs("a")