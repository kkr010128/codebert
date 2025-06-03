
_ = input()
N = sorted([int(v) for v in input().split()])
s = 1
for n in N:
    s *= n
    if s == 0 or s > 10**18:
        break

print(s if s <= 10**18 else -1)