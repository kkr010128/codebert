N, M = map(int, input().split())
S = input()

ans = []

now_pos = N

while now_pos > 0:
    next_pos = max(0, now_pos - M)
    for i in range(M):
        if S[next_pos + i] == "0":
            ans.append(now_pos - (next_pos + i))
            now_pos = next_pos + i
            break
    else:
        print(-1)
        exit()

print(" ".join(map(str, ans[::-1])))
