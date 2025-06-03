input()
A = input().split()
a_set = set(A)
if len(A) == len(a_set):
    print('YES')
else:
    print('NO')