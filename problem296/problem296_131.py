s = list(input())
k = int(input())
n = len(s)

if s == [s[0]]*n:
    print(n*k//2)
else:
    ss = s*2
    ans1 = 0
    for i in range(1, n):
        if s[i] == s[i -1]:
            s[i] = ""
            ans1 += 1
    ans2 = 0
    for i in range(1, 2*n):
        if ss[i] == ss[i - 1]:
            ss[i] = ""
            ans2 += 1
    j = ans2 - ans1
    print(ans1 + j*(k - 1))