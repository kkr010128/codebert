N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
print('Yes' if M <= len(list(filter(lambda x: x, map(lambda x: x * 4 * M >= total, A)))) else 'No')