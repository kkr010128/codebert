a_len = int(input())
a_ar = sorted([int(n) for n in input().split(" ")])
b_len = int(input())
b_ar = [int(n) for n in input().split(" ")]
dp = [0 for n in range(2001)]
for a in a_ar:
    new_dp = dp[:]
    new_dp[a] = 1
    for i,d in enumerate(dp):
        if d and i + a <= 2000:
            new_dp[i + a] = 1
    dp = new_dp
for b in b_ar:
    if dp[b]:
        print("yes")
    else:
        print("no")