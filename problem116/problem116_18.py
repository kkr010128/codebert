S = list(str(input()))
T = list(str(input()))
tt = 0
cnt = 0

for i in S:
    if i != T[tt]:
        cnt += 1
    tt += 1

print(cnt)
