def Reverse(str, A, B):
    a = int(A)
    b = int(B)
    if a == 0:
        str = str[0:a] + str[b::-1] + str[b + 1:]
    else:
        str = str[0:a] + str[b:a - 1:-1] + str[b + 1:]
    return str

def Replace(str, a, b, c):
    str2 = ''
    Str = list(str)
    for i in range(int(b) - int(a) + 1):
        Str[i + int(a)] = c[i]
    for i in range(len(Str)):
        str2 += Str[i]
    return str2

str = input()
n = int(input())
for i in range(n):
    a = input()
    A = a.split()
    if A[0] == 'print':
        print(str[int(A[1]):int(A[2]) + 1])
    elif A[0] == 'reverse':
        str = Reverse(str, A[1], A[2])
    elif A[0] == 'replace':
        str = Replace(str, A[1], A[2], A[3])

