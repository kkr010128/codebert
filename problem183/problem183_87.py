n = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# その数自身
ans = 1
# 1以外のn-1の約数
ans += len(make_divisors(n-1)) - 1

d = make_divisors(n)
for k in range(1,(len(d)+1)//2):
    i = d[k]
    j = n//i
    while j % i == 0:
        j //= i
    if j % i == 1:
        ans += 1

print(ans)