n = int(input())

memo = {}

for _ in range(n):
    s = input()
    try:
        memo[s] += 1
    except KeyError:
        memo[s] = 1

m = max(memo.values())

print(*sorted([ i for i, j in memo.items() if j == m]), sep='\n')
