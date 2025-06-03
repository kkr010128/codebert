S = input()
N = len(S)
count = 0
n = N//2
for i in range(n):
    if S[i] != S[N-1-i]:
        count +=1
print(count)