n = int(input())
s = input()

ok = [0,0,0,0,0,0,0,0,0,0]
ans = 0

for i in range(n):
    if sum(ok) == 10:
        break
    if ok[int(s[i])] == 1:
        continue
    ok[int(s[i])] = 1
    nd = [0,0,0,0,0,0,0,0,0,0]
    for j in range(i+1,n):
        if sum(nd) == 10:
            break
        if nd[int(s[j])] == 1:
            continue
        nd[int(s[j])] = 1
        rd = [0,0,0,0,0,0,0,0,0,0]
        for k in range(j+1, n):
            if sum(rd) == 10:
                break
            if rd[int(s[k])] == 1:
                continue
            rd[int(s[k])] = 1
            ans += 1

print(ans)
