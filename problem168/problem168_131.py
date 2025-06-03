n, m = (int(x) for x in input().split())
list_a = [int(x) for x in input().split()]

for i in range(0, m):
    n -= list_a[i]
    if n < 0:
        print('-1')
        exit()
print(n)