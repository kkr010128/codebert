a, b = [int(tem) for tem in input().split()]

def mak(A, B) :
    while B != 0 :
        q, r = divmod(A, B)
        A = int((A - r) / q)
        B = r
    return A

if a > b : print(mak(a, b))
else     : print(mak(b, a))