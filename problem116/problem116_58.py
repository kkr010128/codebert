S=list(input())
T=list(input())
total = 0
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        total += 1
print(str(total))