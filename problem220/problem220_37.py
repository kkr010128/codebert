S, T = map(str,input().split())
A, B = map(int,input().split())
U = str(input())

if S == U:
    A -= 1
    l = [A,B]
    print(' '.join(map(str,l)))
elif T == U:
    B -= 1
    l = [A, B]
    print(' '.join(map(str, l)))