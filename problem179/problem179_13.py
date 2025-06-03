n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
n_vote = sum(l)
if l[m-1] >= n_vote/(4*m):
    print('Yes')
else:
    print('No')