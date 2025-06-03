N, M = map(int, input().split())
a = list(map(int, input().split()))
homework = 0

for i in range(M):
    homework += a[i]

play = N - homework

if play < 0:
    print(-1)
else:
    print(play)