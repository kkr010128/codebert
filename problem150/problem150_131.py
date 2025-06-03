n,k = map(int,input().split())
a = list(map(int,input().split()))

tt = [0] * n
tt[0] = 1
ans_l = [1]
i = 1
c = 0

while True:
    if c == k: #ループに達することができないk回を入力として与えられるとこの条件式がない場合
        break  #ループに達した上で計算されてしまう。これがあるとkが下の式で0として計算される。
    c += 1
    i = a[i-1]
    if tt[i-1] == False:
        tt[i-1] = 1
        ans_l.append(i)
    else:
        break

#print(c,k)
d = ans_l.index(i)
k -= d
ans = k % (len(ans_l)-d)
print(ans_l[ans+d])
