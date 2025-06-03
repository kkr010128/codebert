def eq1(A,B,x):
    temp = (A*x)
    temp //= B
    return temp

def eq2(A,B,x):
    temp = x//B
    temp = temp*A
    return temp

def main():
    A,B,N = map(int,input().split())

    if B <= N:
        x = B-1
        ans = eq1(A,B,x) - eq2(A,B,x)
        return ans
    else:
        x = N
        ans = eq1(A,B,x) - eq2(A,B,x)
        return ans

print(main())
