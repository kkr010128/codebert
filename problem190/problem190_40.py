def kaibun(moji):
    n = len(moji)
    for i in range(0,int(n/2)):
        if s[i]!=s[n-1-i]:
            return False
    return True

s = str(input())
n = len(s)
moji1 = int((n - 1) / 2)
moji2 = int((n + 3) / 2)
#print(s[:moji1])
#print(s[moji2-1:])
if kaibun(s) and kaibun(s[:moji1]) and kaibun(s[moji2-1:]):
    print('Yes')
else:
    print('No')