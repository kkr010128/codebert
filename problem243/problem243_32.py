N = int(input())
clips = [input().split() for _ in range(N)]
X = input()
ans = 0

for i,title in enumerate(clips):
    if X in title:
        for j in range(i+1, N):
            ans += int(clips[j][1])
        break

print(ans)