n = int(input())
a = list(filter(lambda x : x & 1 or x % 3 == 0 or x % 5 == 0, map(int, input().split())))
print('APPROVED' if len(a) == n else 'DENIED')