n, k = map(int, input().split())
MOD = 10 ** 9 + 7

patterns = [0] * k
total = 0

for i in range(k, 0, -1):
    # gcdがちょうどi ⇔ すべての要素がiの倍数
    # かつ　すべての要素が2i, 3i, ...の倍数でない
    tmp = pow(k // i, n, MOD)

    for j in range(2*i, k+1, i):
        tmp -= patterns[j-1]
    
    patterns[i-1] = tmp
    total += i * tmp
    total %= MOD

print(total)
