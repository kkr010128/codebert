N =int(input())

A = sorted(list(map(int,input().split())))

B = 1
C = 10 ** 18

for i in range(N):
    B = B * A[i]
    if B == 0:
        break
    elif B > C:
        B = -1
        break

print(B)
    
