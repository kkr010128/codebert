s, t = input().split()
a, b = map(int, input().split())
u = input()

bnum = {s: a, t: b}
bnum[u] -= 1
print('{} {}'.format(bnum[s], bnum[t]))
