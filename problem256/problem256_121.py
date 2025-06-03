def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 

def lcm(a,b): 
    return (a*b) / gcd(a,b) 

if __name__ == "__main__":
    n1,n2=map(int,input().split(' '))
    print(int(lcm(n1,n2)))