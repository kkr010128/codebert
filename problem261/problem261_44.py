s = list(input())
ans = 0
halfidx = int((len(s)/2))
ary  = s[0:halfidx]
rary = list(reversed(s))[0:halfidx]
for i in range(0,halfidx):
    if (ary[i] != rary[i]):
        ans = ans + 1
print(ans)