N = int(input())
A = list(map(int, input().split()))


A.sort()
A.append(N + 1)
ans = [0] * (N+1)
count = [0, 0]

for i in range(N):
    if count[0] == A[i]:
        count[1] += 1
    else:
        ans[count[0]] = count[1]
        count[0] = A[i]
        count[1] = 1

for j in range(1, N+1):
    print(ans[j])