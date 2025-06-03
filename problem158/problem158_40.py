K = int(input())
A, B = map(int, input().split())

a, mod_a = divmod(A, K)
b, mod_b = divmod(B, K)

if mod_a == 0 or mod_b == 0:
    print('OK')
    exit()

if a == b:
    print('NG')
else:
    print('OK')
