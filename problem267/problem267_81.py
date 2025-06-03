N = int(input())
S = input()

ans = 0
for i in range(1000):
    s = ["0", "0", "0"]
    s[0] = str(i // 100)
    s[1] = str((i//10) % 10)
    s[2] = str(i % 10)

    ind = 0
    cnt = 0
    while cnt < 3 and ind < N:
        if S[ind] == s[cnt]:
            cnt += 1
        ind += 1

        if cnt == 3:
            ans += 1

print(ans)
