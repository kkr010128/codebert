n, k = map(int,input().split())
a = list(map(int, input().split()))
flg = [True] * n
dst = [1]
twn = 0
for _ in range(k):
    if flg[twn]:
        dst.append(a[twn])
        flg[twn] = False
        twn = a[twn] - 1
    else:
        index = dst.index(a[twn])
        ld = len(dst[:index])
        cyc = len(dst[index:])
        print(dst[(ld - 1) + (k + 1 - ld) % cyc] if (k + 1 - ld) % cyc != 0 else dst[-1])
        exit()
print(dst[-1])