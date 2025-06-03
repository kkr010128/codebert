n, m = (int(x) for x in input().split())
list_a = sorted([int(x) for x in input().split()], reverse=True)

for i in range(0, m):
    if list_a[i] < sum(list_a) / (4 * m):
        print('No')
        exit()
print('Yes')