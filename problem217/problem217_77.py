import sys

S = int(next(sys.stdin))
A = map(int, next(sys.stdin).strip().split())
even_numbers = filter(lambda y: not y % 2, A)
print('APPROVED' if all(not v % 3 or not v % 5 for v in even_numbers) else 'DENIED')