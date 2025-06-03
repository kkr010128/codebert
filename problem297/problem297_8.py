def resolve():
    N = int(input())
    print((N//2+1)/N if N%2==1 else 0.5)
    
if '__main__' == __name__:
    resolve()