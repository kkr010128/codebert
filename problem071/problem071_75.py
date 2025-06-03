S = list(input())

if S[-1] != "s":
    S.append("s")

else:
    S.append("es")

print(*S, sep="")