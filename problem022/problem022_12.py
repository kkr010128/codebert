
def LinearSearch1(S, n, t):
    for i in range(n):
        if S[i] == t:
            return i
            break
    else:
        return -1

"""
def LinearSearch2(S, n, t):
    S.append(t)
    i = 0

    while S[i] != t:
        i += 1

    S.pop()
    if i == n:
        return -1
    else:
        return i
"""

n = int(input())
S = [int(s) for s in input().split()]

q = int(input())
T = {int(t) for t in input().split()}

ans = sum(LinearSearch1(S, n, t) >= 0 for t in T)

print(ans)