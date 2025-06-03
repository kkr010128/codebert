import sys
input = sys.stdin.readline

n, s, f = int(input()), list(map(int, input().split())), True
for e in s:
  if not e & 1:
    if 0 not in [e % 3, e % 5]: f = False; break
print('APPROVED' if f else 'DENIED')
