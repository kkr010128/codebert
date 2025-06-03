A, B = input().split()
A = int(A)
B = int(B.replace('.',''))
print(f'{A*B//100}')