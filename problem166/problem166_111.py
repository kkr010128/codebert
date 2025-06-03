from collections import Counter

S = input()
MOD = 2019
div10 = 202  # modInverse(10, MOD). Note MOD is not prime so can't use FLT!


def solve1(S):
    # Naive implementation
    counts = [0 for i in range(MOD)]
    total = 0
    for d in S:
        d = int(d)
        nextCounts = [0 for i in range(MOD)]
        nextCounts[d] += 1
        for k, v in enumerate(counts):
            nextCounts[(10 * k + d) % MOD] += v
        counts = nextCounts
        total += counts[0]
    return total


def solve2(S):
    # Instead of shuffling the entire counts, update how we index into counts instead
    # The cumulative shuffle function forward is something like a * index + b for some calculable a, b
    # Then indexing into counts[t][x] is same as indexing into counts[0][(x - b) / a]

    negPowTen = 1  # our a
    prefix = 0  # our b
    counts = [0 for i in range(MOD)]
    total = 0
    for d in S:
        d = int(d)
        prefix = (10 * prefix + d) % MOD
        negPowTen = (negPowTen * div10) % MOD
        counts[((d - prefix) * negPowTen) % MOD] += 1
        total += counts[((0 - prefix) * negPowTen) % MOD]
    return total


def solve3(S):
    # Alternative solution, precompute prefixes, p[i+1] == (10 * p[i] + S[i]) % MOD
    # Then you have for S = '1817181712114'
    # p[1] = 1
    # p[2] = 18
    # p[3] = 181
    # p[4] = 1817
    # etc
    # Then want to count all i j such that:
    # (p[j] - p[i] * pow(10, j - i)) % M == 0
    # Which is equivalent to
    # (p[j] * pow(10, -j) - p[i] * pow(10, -i) % M == 0
    negPowTen = 1
    total = 0
    prefix = 0
    counts = [0 for i in range(MOD)]
    counts[0] = 1
    for d in S:
        prefix = (prefix * 10 + int(d)) % MOD
        key = (prefix * negPowTen) % MOD
        total += counts[key]
        counts[key] += 1
        negPowTen = (negPowTen * div10) % MOD

    return total


def solve4(S):
    # Compute all suffixes instead
    # S     = '1817181712114'
    # suf[1] =             4
    # suf[2] =            14
    # suf[3] =           114
    # suf[4] =          2114
    #
    # Difference of suffixes is almost correct but has extra 10s.
    # For example 2114 to 114 is the string 2 but our difference returns 2000.
    # Luckily 2 and 5 aren't divisible by 2019 so the extra 10s don't matter when counting.
    N = len(S)
    suf = 0
    powTen = 1
    counts = [0 for i in range(MOD)]
    total = 0
    counts[0] = 1
    for i in range(N):
        d = int(S[N - 1 - i])
        suf = (powTen * d + suf) % MOD
        total += counts[suf]
        counts[suf] += 1
        powTen = (powTen * 10) % MOD
    return total


#assert solve1(S) == solve2(S) == solve3(S) == solve4(S)
ans = solve4(S)
print(ans)
