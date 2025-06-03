h, n = map(int, input().split())
a = [int(x) for x in input().split()]

print('Yes' if h<=sum(a) else 'No')