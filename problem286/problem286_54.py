A, B = map(int, input().split())
if A>=10 or B>=10:
    print('-1')
    exit()
else:
    print(A*B)