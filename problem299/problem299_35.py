def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ords = []
    for i, a in enumerate(A):
        ords.append((i, a))
    ans = list(map(lambda x: x[0]+1, sorted(ords, key=lambda x: x[1])))
    print(*ans)
    
        
    


    
if '__main__' == __name__:
    resolve()