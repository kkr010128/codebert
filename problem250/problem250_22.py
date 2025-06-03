import math
X = int(input())

def is_prime(x):
    a = int(math.sqrt(X)) + 1#ある数が素数かどうかはO(√A)で判定できる
    for i in range(2,a):
        if x % i == 0:
            return False
    return True#xは素数

for j in range(X,10**5+4):
    if is_prime(j):
        ans = j    
        break
print(ans)