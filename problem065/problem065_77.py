A = 0
W = str(input())
while True:
    T = str(input())
    if T == 'END_OF_TEXT':
        break
    T = (T.lower().split())
    a = (T.count(W))
    A = A + a
print(A)
