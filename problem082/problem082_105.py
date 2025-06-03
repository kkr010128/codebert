S = input()
T = input()

lt, ls = len(T), len(S)

def diff(s1, s2):
    d = len(s1)

    d -= len([i for i,j in zip(s1, s2) if i == j])
    return d

dlen = min([diff(T, S[i:i+lt]) for i in range(ls) if i + lt <= ls])

print(dlen)
