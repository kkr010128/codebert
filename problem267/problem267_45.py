N = int(input())
S = input()
ans = 0
for x in range(10):
    for y in range(10):
        for z in range(10):
            for i in range(N):
                if x != int(S[i]):
                    continue
                for j in range(i+1, N):
                    if y != int(S[j]):
                        continue
                    for k in range(j+1, N):
                        if z != int(S[k]):
                            continue
                        ans += z == int(S[k])
                        break
                    break
                break
print(ans)
