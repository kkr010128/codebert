n = int(input())
s = input()
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            fi = False
            fj = False
            for ss in s:
                ss = int(ss)
                if not fi and ss == i:
                    fi = True
                    continue
                if fi and not fj and ss == j:
                    fj = True
                    continue
                if fj and ss == k:
                    ans += 1
                    break
print(ans)
