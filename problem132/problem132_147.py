n,k_ = map(int,input().split())
a_li = list(map(int,input().split()))
a_li_o = [0]*n
for i in range(k_):
    for l in range(n):
        a_li_o[l] = a_li[l]
    dum_li = [0]*n
    for j in range(n):
        left = j - a_li[j]
        right = j + a_li[j] + 1
        if left < 0:
            left = 0
        dum_li[left] += 1
        if right > n-1:
            continue
        dum_li[right] -= 1
    total = 0
    for k in range(n):
        total += dum_li[k]
        dum_li[k] = total
    for k in range(n):
        a_li[k] = dum_li[k]
    if a_li_o == a_li:
        break
print(" ".join(map(str,a_li)))