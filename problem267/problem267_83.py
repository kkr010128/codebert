N = int(input())
S = input()
cnt = 0

for i in range(10):
    x100 = S.find(str(i))
    if x100 == -1:
        continue
    for j in range(10):
        x10 = S.find(str(j), x100 + 1)
        if x10 == -1:
            continue
        for k in range(10):
            if S.find(str(k), x10 + 1) != -1:
                cnt += 1

print(cnt)
