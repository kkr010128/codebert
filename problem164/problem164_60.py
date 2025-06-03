A, B, C, D = map(int, input().split())

if C % B == 0:
    Takahashi_attacks = C // B
else:
    Takahashi_attacks = C // B + 1

if A % D == 0:
    Aoki_attacks = A // D
else:
    Aoki_attacks = A // D + 1



if Takahashi_attacks <= Aoki_attacks:
    print('Yes')
else:
    print('No')