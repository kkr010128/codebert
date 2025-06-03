n, m = map(int, input().split())
a = [int(x) for x in input().split()]
s = sum(a)

print('Yes' if len(list(filter(lambda x : x >= s * (1/(4*m)), a))) >= m else 'No')