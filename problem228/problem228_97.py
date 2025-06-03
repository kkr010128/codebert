import  math

def pow(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

H = int(input())

#print(int(math.log2(H)))
print(pow(2,int(math.log2(H))+1)-1)
