allst = list(input().split())
stk = []
ans = 0
for i in range(0, len(allst)):
    if allst[i] == '+':
        stk[len(stk)-2] = stk[len(stk)-2] + stk[len(stk)-1]
        del stk[len(stk)-1]
    elif allst[i] == '-':
        stk[len(stk)-2] = stk[len(stk)-2] - stk[len(stk)-1]
        del stk[len(stk)-1]
    elif allst[i] == '*':
        stk[len(stk)-2] = stk[len(stk)-2] * stk[len(stk)-1]
        del stk[len(stk)-1]
    else:
        stk.append(int(allst[i]))
print(stk[len(stk)-1])