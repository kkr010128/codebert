import sys, math

max_int = 1000000001  # 10^9+1
min_int = -max_int

n = int(sys.stdin.readline())
positive_counter = {}
negative_counter = {}
to_add = 0
a_zero_counter = b_zero_counter = 0
for _n in range(n):
    s = sys.stdin.readline()
    a, b = map(int, s.split())

    if a == 0 and b == 0:
        to_add += 1
        continue
    elif a == 0:
        a_zero_counter += 1
        continue
    elif b == 0:
        b_zero_counter += 1
        continue
    elif (a > 0) == (b > 0):
        a = abs(a)
        b = abs(b)
        gcd = math.gcd(a, b)
        definer = (a // gcd, b // gcd)

        if definer not in positive_counter:
            positive_counter[definer] = 1
        else:
            positive_counter[definer] += 1
    else:
        a = abs(a)
        b = abs(b)
        gcd = math.gcd(a, b)
        definer = (b // gcd, a // gcd)

        if definer not in negative_counter:
            negative_counter[definer] = 1
        else:
            negative_counter[definer] += 1

prod = 2 ** a_zero_counter + 2 ** b_zero_counter - 1
#print(positive_counter, negative_counter)
for k in positive_counter:
    if k in negative_counter:
        prod *= 2 ** positive_counter[k] + 2 ** negative_counter[k] - 1
        negative_counter.pop(k)
    else:
        prod *= 2 ** positive_counter[k]
    prod %= 1000000007

for k in negative_counter:
    prod *= 2 ** negative_counter[k]
    prod %= 1000000007

prod += to_add - 1

print(prod % 1000000007)
