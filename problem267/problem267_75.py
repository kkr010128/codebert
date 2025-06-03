N = int(input())
S = str(input())
num = []
for _ in range(10):
    num.append([])

for i in range(N):
    num[int(S[i])].append(i)

ans = 0
for X1 in range(0, 10):
    for X2 in range(0, 10):
        for X3 in range(0, 10):
            X = str(X1) + str(X2) + str(X3)
            if num[X1] != [] and num[X2] != [] and num[X3] != []:
                if num[X1][0] < num[X2][-1]:
                    for i in num[X2]:
                        if num[X1][0] < i < num[X3][-1]:
                            ans += 1
                            break

print(ans)
