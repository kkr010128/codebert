S = list(input())
T = list(input())

i = 0
ans =[]

while i + len(T) <= len(S):
    n = 0
    for s, t in zip(S[i:i+len(T)], T):
        if s != t:
            n += 1
    ans.append(n)
    i += 1

print(min(ans))