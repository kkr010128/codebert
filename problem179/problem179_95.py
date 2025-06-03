n, m = map(int, input().split())
lis = sorted(list(map(int, input().split())), reverse=True)
limit = sum(lis) / (4 * m)
judge = 'Yes'
for i in range(m):
    if lis[i] < limit:
        judge = 'No'
        break
print(judge)