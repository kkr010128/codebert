ab = [int(x) for x in input().split()]

# Naive Algorithm
# m = min(ab)
# gcd = 1
# for i in range(2, int(m/2)):
#     if ab[0] % i == 0 and ab[1] % i == 0:
#         gcd = i
# print(gcd)

# Euclidean Algorithm
while True:
    min_i = ab.index(min(ab))
    max_i = ab.index(max(ab))
    r = ab[max_i] % ab[min_i]
    if r == 0:
        print(ab[min_i])
        break
    else:
        ab[max_i] = r