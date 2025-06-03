K = int(input())
A, B = map(int, input().split())
if A % K == 0 or B % K ==0:
    print('OK')
elif int(B/K) - int(A/K) >= 1:
    print('OK')
else:
    print('NG')