K = int(input())
S = list(input())
if len(S) <= K:
    print(*S,sep="")
else:
    S2 = S[:K]
    S2.append("...")
    print(*S2,sep="")