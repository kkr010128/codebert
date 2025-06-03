def solve(n, m, s):
    if s.find("1"*m) >= 0:
        return -1
    s = s[::-1]
    i = 0
    path = []
    while i < n:
        for j in range(min(m, n-i), 0, -1):
            ni = i+j
            if s[ni] == "0":
                i = ni
                path.append(j)
                break
    return " ".join(map(str, path[::-1])) 

n, m = map(int, input().split())
s = input()
print(solve(n, m, s))