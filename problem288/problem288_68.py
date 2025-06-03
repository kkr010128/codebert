import math
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

n = int(input())
yaku = make_divisors(n)

Min = float('inf')
for i in range(math.ceil(len(yaku)/2)):
    Min = min(Min, yaku[i]+yaku[-(i+1)])

print(Min-2)