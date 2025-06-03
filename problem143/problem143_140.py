k = int(input())
s = list(input())
an_lis = []
if len(s) <= k:
    ans = "".join(s)
    print(ans)
else:
    for i in range(k):
        an_lis.append(s[i])
    an_lis.append("...")
    ans = "".join(an_lis)
    print(ans)
