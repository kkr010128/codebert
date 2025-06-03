n = int(input())
a = ord("a")

def dfs(s, mx):
    if len(s) == n:
        print(s)
    else:
        for i in range(a, mx + 2):
            if i != mx + 1:
                dfs(s + chr(i), mx)
            else:
                dfs(s + chr(i), mx + 1)

dfs("a", a)