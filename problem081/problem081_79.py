# A - Don't be late

D, T, S = map(int, input().split())

if (D + S - 1) // S <= T:
    print('Yes')
else:
    print('No')