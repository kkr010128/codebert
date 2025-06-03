X = int(input())

# If a is positive: n ** 5 - (n - 1) ** 5 exceeds 10 ** 9 when i = 120
# If a is non-positive: n ** 5 - (n - 1) ** 5 exceeds 10 ** 9 when i = -119
# So, the valid range of A is from -118 to 119
for a in range(-118, 119 + 1):
    tgt = a ** 5 - X
    for b in range(-119, 119):
        if tgt == b ** 5:
            print(a, b)
            exit()
