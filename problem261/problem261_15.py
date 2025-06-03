S = input()
L = len(S)
L //= 2
answer = 0
for i in range(L):
    if S[i] != S[-i-1]:
        answer += 1
print(answer)