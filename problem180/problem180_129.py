import sys
n, k = list(map(int, input().split()))

if (k == 1):
    print(0)
    sys.exit()

ans = 0
v_ans = 0
if (n > k):
    v_ans = n % k
else:
    v_ans = n

if (abs(v_ans - k) < v_ans):
    ans = abs(v_ans - k)
else:
    ans = v_ans

print(ans)
