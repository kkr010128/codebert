S,T = input().split()
A,B = (int(x) for x in input().split())
U = input()
if U == S:
    A -= 1
    print(('{} {}'.format(A,B)))
else:
    B -= 1
    print(('{} {}'.format(A,B)))