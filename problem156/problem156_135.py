X = int(input())

B_max = int(X**(0.25))

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=(n//i):
                divisors.append(n//i)
    divisors.sort()
    return divisors

divisors = get_divisors(X)

flg = False
for div in divisors:
    for B in range(-B_max, B_max+1):
        A = B + div
        A4_B4 = A**4 + A**3 * B + A**2 * B**2 + A * B**3 + B**4
        
        if (div * A4_B4 == X):
            flg = True
            break
    
    if flg:
        break


print("{} {}".format(A, B))