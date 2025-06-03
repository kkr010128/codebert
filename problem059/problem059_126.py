r, c = map(int, input().strip().split())
l = [[0 for j in range(c+1)] for i in range(r+1)]
for i in range(r):
    l[i] = list(map(int, input().strip().split()))
    l[i].append(sum(l[i][0:c]))
    l[r] = [l[r][j] + l[i][j] for j in range(c+1)]
    print(' '.join(map(str,l[i])))
print(' '.join(map(str,l[r])))