import math

a, b, c, d = map(int, input().split())

takahashi_attacks = math.ceil(c / b)
aoki_attacks = math.ceil(a / d)

if takahashi_attacks <= aoki_attacks:
    print('Yes')
else:
    print('No')