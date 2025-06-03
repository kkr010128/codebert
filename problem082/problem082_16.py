S = input()
T = input()

max_match = 0

n = len(T)
m = len(S)

for i in range(m-n+1):
    tmp = 0
    for j in range(i,i+n):
        if S[j] == T[j-i]:
            tmp += 1
    if tmp > max_match:
        max_match = tmp

ans = n - max_match



print(ans)