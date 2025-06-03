def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            upper_divisors.append(n//i)
        i += 1
    return lower_divisors, upper_divisors


n = int(input())
low, up = make_divisors(n)
if len(low) != 1:
    # ans = low[0] + up[0]
    # for i in range(1, len(low)):
    #     tmp = low[i] + up[i]
    #     if tmp < ans:
    #         ans = tmp
    print(low[-1] + up[-1] - 2)
else:
    print(n - 1)
