T = list(input())


ans = 0
for i in range(len(T)):
    if T[i]=="?":
        T[i]="D"

print(*T, sep="")