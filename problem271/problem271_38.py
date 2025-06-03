N = int(input())
S = list(input())
alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
S_a = ""
for s in S:
    n = alp.index(s)+N 
    if(alp.index(s)+N>=26):
        n -= 26
    S_a += alp[n]
print(S_a)