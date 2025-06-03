S = input()
T = input()

# S = "cabacc"
# T = "abc"

lt = len(T)

def diff(s1, s2):
    d = len(s1)

    d -= len([i for i,j in zip(s1, s2) if i == j])
    return d

dlen = 1000000000
for i in range(len(S)):
    if i + lt <= len(S):
        dlen = min(dlen, diff(T, S[i:i+lt]))

print(dlen)
