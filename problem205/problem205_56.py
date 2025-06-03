n, p = map(int, input().split())
s = input()
sum_count = 0
if p in {2, 5}:
    for right in range(n):
        if int(s[right]) % p == 0:
            sum_count += (right + 1)
else:
    modp_count = [0] * p
    modp_count[0] = 1
    subs_modp, pow = 0, 1
    for si in s[::-1]:
        subs_modp += ((int(si)*pow) % p)
        subs_modp %= p
        modp_count[subs_modp] += 1
        pow = (pow*10) % p
        
    for count in modp_count:
        sum_count += count*(count - 1) // 2
print(sum_count)