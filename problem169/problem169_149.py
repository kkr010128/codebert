n = int(input())
cnt = [0] * (n+100)
A = list(map(int, input().split()))
for a in A:
    cnt[a] += 1
for i in range(n):
    print(cnt[i+1])
