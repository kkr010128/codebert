a1, a2, a3 = map(int, input().split())
x = a1 + a2 + a3
print('win' if x <= 21 else 'bust')