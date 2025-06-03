N, A, B = map(int, input().split())
if (A + B) % 2 == 0:
    print(B - (A + B) // 2)
    exit()
to1 = A - 1
toN = N - B
if to1 < toN:
    B -= to1 + 1
    print(to1 + 1 + B - (1 + B) // 2)
else:
    A += toN + 1
    print(toN + 1 + N - (A + N) // 2)
