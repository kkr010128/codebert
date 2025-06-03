import math
def factrization_prime(number):
    factor = {}
    div = 2
    s = math.sqrt(number)
    while div < s:
        div_cnt = 0
        while number % div == 0:
            div_cnt += 1
            number //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if number > 1:
        factor[number] = 1
    return factor

N = int(input())
v = list(factrization_prime(N).values())
ans = 0
for i in range(len(v)):
    k = 1
    while(True):
        if v[i] >= k:
            v[i] -= k
            k += 1
            ans += 1
        else:
            break
print(ans)
