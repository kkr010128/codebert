N = int(input())
S = input()

ans = 0
tmp = [0 for _ in range(10)]
for i in range(len(S)):
    tmp[int(S[i])] += 1

for i in range(1000):
    flag = True

    if i < 10:
        dic = {"0": 2}
    elif i < 100:
        dic = {"0": 1}
    else:
        dic = {}
    for j in range(len(str(i))):
        if str(i)[j] in dic:
            dic[str(i)[j]] += 1
        else:
            dic[str(i)[j]] = 1

    for k, v in dic.items():
        if dic[k] > tmp[int(k)]:
            flag = False
            break

    if flag:
        if i < 10:
            tmp_i = "00" + str(i)
        elif i < 100:
            tmp_i = "0" + str(i)
        else:
            tmp_i = str(i)
        t = 0
        for j in range(len(S)):
            if tmp_i[t] == S[j]:
                t += 1
            if t == 3:
                ans += 1
                break

print(ans)

