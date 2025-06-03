n = int(input())

memo = {}
for i in range(n):
    man_idx = i
    count = int(input())
    comment = [ list(map(int,input().split())) for _ in range(count) ]
    memo[man_idx] = comment

ans = 0
for i in range(2**n):
    sub_ans = 0
    is_true = True
    for j in range(n):
        if i >> j & 1:
            sub_ans += 1
            for x, y in memo[j]:
                if (i >> (x-1) & 1)  !=  int(y):
                    is_true = False
                    break
    if is_true:
        ans = max(sub_ans, ans)
print(ans)