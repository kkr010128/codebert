import bisect
N = int(input())
L = list(map(int,input().split()))
L = sorted(L,reverse = False)

cnt = 0
# a の index
for a in range(len(L)):
    # b の index
    for b in range(a+1,len(L)):
        # c が取りうる最大の index
        c_idx = bisect.bisect_left(L,L[a]+L[b]) - 1
        cnt += c_idx - b
print(cnt)