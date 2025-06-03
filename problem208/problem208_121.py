N, M = map(int, input().split())
SC = list(tuple(map(int, input().split())) for _ in range(M))

for i in range(10**N):
    if len(str(i)) == N and all(str(i)[s-1] == str(c) for s, c, in SC):
        print(i)
        break
else:
    print(-1)
