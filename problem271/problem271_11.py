N = int(input())
S = input()
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
for i in S:
    ind = A.index(i)
    ind += N
    if ind > 25:
        ind -= 26
    result += A[ind]
print(result)