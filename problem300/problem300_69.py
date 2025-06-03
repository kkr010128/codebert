def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    def gcd(x,y):
        r = x%y
        if r==0:
            return y

        return gcd(y, r)

    a, b  = map(int, input().split())
    c = gcd(a, b)

    tmp = c
    cnt = 1
    for i in range(2, int(c**0.5)+1):

        if tmp%i == 0:
            cnt += 1
            while tmp%i == 0:
                tmp /= i
    if tmp != 1:
        cnt += 1
    print(cnt) 

            
            
    




    
    
if __name__ == '__main__':
    main()