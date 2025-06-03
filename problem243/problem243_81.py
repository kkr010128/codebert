N = int(input())
music = []
time = []
for i in range(N):
    m,t = input().split()
    music.append(m)
    time.append(int(t))

S = input()
ans = 0
ans += sum(time[music.index(S)+1:])
print(ans)