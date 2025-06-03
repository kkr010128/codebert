import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

H = ri()
cnt = 1
while H > 1:
    H = H // 2
    cnt += 1
print(sum([2 ** i for i in range(cnt)]))