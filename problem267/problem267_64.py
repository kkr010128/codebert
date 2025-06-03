N = int(input())
S = input()

ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            s = ["0", "0", "0"]
            s[0] = str(i)
            s[1] = str(j)
            s[2] = str(k)

            ind = 0
            cnt = 0
            while cnt < 3 and ind < N:
                if S[ind] == s[cnt]:
                    cnt += 1
                ind += 1

                if cnt == 3:
                    ans += 1

print(ans)
