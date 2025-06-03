n = int(input())
s = input()

rinds, ginds, binds = [], [], set()

for i in range(n):
    if s[i] == 'R': rinds.append(i)
    elif s[i] == 'G': ginds.append(i)
    else: binds.add(i)

rlen, glen, blen = len(rinds), len(ginds), len(binds)


ans = 0

for i in rinds:
    for j in ginds:
        dist = abs(i-j)
        i_ = min(i, j)
        j_ = max(i, j)
        ans += blen
        # i' < j' < k
        if j_ + dist in binds:
            ans -= 1
        if dist%2==0 and i_ + dist//2 in binds:
            ans -= 1
        if i_ - dist in binds:
            ans -= 1

        # if binsearch_same(binds, blen, dist, j_):
        #     ans -= 1
        # # i'< k < j' 
        # if dist%2==0 and binsearch_same(binds, blen, dist//2, i_):
        #     ans -= 1
        # # # k < i' < j'
        # if binsearch_same(binds, blen, -dist, i_):
        #     ans -= 1

print(ans)















# n = input()
# print('Yes' if '7' in n else 'No')

# n = int(input())
# ans = 0
# for i in range(1, n+1):
#     if i%3 == 0 or i%5==0:
#         pass
#     else:
#         ans += i
# print(ans)


# k = int(input())
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# ans = 0
# for a in range(1, k+1):
#     for b in range(1, k+1):
#         for c in range(1, k+1):
#             ans += gcd(gcd(a, b), c)
# print(ans)