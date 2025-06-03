N = int(input())
S = input()

ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            tmp = 0
            for l, value in enumerate(S):
                if tmp == 0:
                    if value == str(i):
                        tmp = 1
                elif tmp == 1:
                    if value == str(j):
                        tmp = 2
                elif tmp == 2:
                    if value == str(k):
                        ans += 1
                        break
print(ans)