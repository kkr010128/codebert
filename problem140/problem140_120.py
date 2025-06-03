T = list(input())
N = len(T)
count = 0
for i in range(N):
    if T[i] == '?':
        T[i] = 'D'
    if (i < N - 1) and T[i] == 'P' and T[i + 1] == 'D':
        count += 1
    elif T[i] == 'D':
        count += 1

#print(count)
ans = ''.join(T)
print(ans)