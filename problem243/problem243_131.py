import sys

input = sys.stdin.readline
N = int(input())
musics = []
for _ in range(N):
    s, t = input().split()
    musics.append((s.strip(), int(t)))

X = input().strip()
ans = 0
flag = False
for s, t in musics:
    if flag:
        ans += t
    if s == X:
        flag = True

print(ans)