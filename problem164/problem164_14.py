from math import ceil

A_HP, A_ATK, B_HP, B_ATK = map(int, input().split())
print('Yes' if ceil(A_HP / B_ATK) >= ceil(B_HP / A_ATK) else 'No')