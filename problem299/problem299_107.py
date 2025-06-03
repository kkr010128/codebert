N = int(input())
A = {int(x): key for key, x in enumerate(input().split(), 1)}
sort_a = sorted(A.items(), key=lambda x: x[0])

print(' '.join([str(key) for x, key in sort_a]))
