A,B,C,D,E,F = map(int, input().split())
q = int(input())

for i in range(q):
    x, y = map(int, input().split())
    while A != x:
        A,B,C,D,E,F = D,B,A,F,E,C #E
        if A == x:
            break
        A,B,C,D,E,F = B,F,C,D,A,E #N
    while B != y:
        A,B,C,D,E,F = A,C,E,B,D,F #R
    print(C)