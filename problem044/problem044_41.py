a, b, c = [int(s) for s in input().split()]
hit = 0
for i in range(a, b + 1):
    if c % i == 0:
        hit += 1
print(hit)