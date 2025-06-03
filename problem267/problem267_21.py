int(input())
s = list(input())
ans = 0
for i in range(10):
    if str(i) in s:
        ss = s[s.index(str(i))+1:]
        for j in range(10):
            if str(j) in ss:
                sss = ss[ss.index(str(j))+1:]
                for k in range(10):
                    if str(k) in sss:
                        ans += 1
print(ans)