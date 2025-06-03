ch = input()
stk1 = []
stk2 = []
ttlar = 0
for i, c in enumerate(ch):
    if c == '\\':
        stk1.append(i)
    elif c == '/' and stk1 != []:
        j = stk1.pop()
        ttlar += i - j
        lar = i - j
        while stk2 != [] and stk2[-1][0] > j:
            lar += stk2.pop()[1]
        stk2.append([j, lar])
print(ttlar)
ans = [len(stk2)]
ans[1:1] = [stk2[i][1] for i in range(len(stk2))]
print(' '.join(map(str, ans)))
