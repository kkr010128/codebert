def get_divisors(n):
    """
    引数の数字の約数を列挙し、setで返します。1および引数自身を含みます。
    計算量はO(log(n))です。
    """
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return divisors


n = int(input())

n_ = get_divisors(n)
n_1 = get_divisors(n - 1)
n_.remove(1)
n_1.remove(1)
n_.difference_update(n_1)
# print(n_)
# print(n_1)
# print(n_.difference(n_1))
ans = len(n_1)
for cand in n_:
    if cand == 2 or cand == n:
        ans += 1
        continue
    tmp = n
    while tmp % cand == 0:
        tmp //= cand
    tmp %= cand
    if tmp == 1:
        ans += 1
print(ans)
