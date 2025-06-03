n,k = map(int, input().split())
hl = list(map(int, input().split()))

hl.sort(reverse=True)

if k >= n:
    print(0)
    exit()

rem_hl = hl[k:]
rem_sum = sum(rem_hl)
print(rem_sum)