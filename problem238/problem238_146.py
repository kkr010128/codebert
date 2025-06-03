n, k, s = map(int, input().split())

ai = s

ls1 = [ai] * k
for aj in reversed(range(10 ** 9 + 1)):
    if aj != ai:
        ls2 = [aj] * (n - k)
        break

print(" ".join(map(str, (ls1 + ls2))))