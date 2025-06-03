def gcd(a,b):
    for i in range(1,min(a,b)+1):
        if a%i ==0 and b % i ==0:
            ans = i
    return ans

x =int(input())
print(360//gcd(360,x))