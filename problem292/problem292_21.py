N = int(input())
d_s = list(map(int, input().split()))
answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        answer += d_s[i] * d_s[j]
print(answer)