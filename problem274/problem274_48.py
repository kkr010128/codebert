N, M = map(int, input().split())
S = input()

index = N
count = 0
history = []
while index > 0:
    start = max(0, index - M)
    for i, c in enumerate(S[start:index], start=start):
        if c == '0':
            history.append(index - i)
            index = i
            count += 1
            break
    else:
        print(-1)
        exit()

print(*history[::-1])