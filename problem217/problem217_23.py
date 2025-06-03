n = int(input())
a = list(map(int, input().split()))
print('APPROVED' if all(ai % 3 == 0 or ai % 5 == 0 for ai in a if ai % 2 == 0) else 'DENIED')