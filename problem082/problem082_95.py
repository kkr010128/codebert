S = str(input())
T = str(input())
s = len(S)
t = len(T)
ans = []
for i in range(s-t+1):
    count = 0
    U = S[i:i+t]
    for j in range(t):
        if U[j] != T[j]:
            count += 1
    ans.append(count)
print(min(ans))