N= int(input())
S = input()

abc = "ABC"
ans = 0
j = 0

for i in range(N):
    if S[i] == abc[j]:
        j += 1
        if S[i] == "C":
            j = 0
            ans += 1
    elif S[i] == "A":
        j = 1
    else:
        j = 0
print(ans)