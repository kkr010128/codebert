n,k = map(int, input().split())
al = list(map(int, input().split()))
fl = list(map(int, input().split()))

al.sort()
fl.sort(reverse=True)
afl = []
for a,f in zip(al,fl):
    afl.append((a,f))

ok, ng = 10**12, -1
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    cnt = 0
    for a,f in afl:
        val = a*f
        train_cnt = (val-mid-1)//f + 1
        cnt += max(train_cnt, 0)

    if cnt <= k:
        ok = mid
    else:
    	ng = mid
print(ok)