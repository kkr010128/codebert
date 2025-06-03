N = int(input())
clips = [input().split() for _ in range(N)]
X = input()
FLG = 0
ans = 0

for title,time in clips:
    if FLG:
        ans += int(time)
    if title == X:
        FLG = 1
    
print(ans)