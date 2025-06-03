# coding: utf-8
# Here your code !
 
def func():
    try:
        (n,m,l) = [ int(item) for item in input().rstrip().split(" ") ]
        matrix_A = [ [ int(item) for item in input().rstrip().split(" ") ] for i in range(n) ]
        matrix_B = [ [ int(item) for item in input().rstrip().split(" ") ] for i in range(m) ]
    except:
        return inputError()
        
    matrix_C = [ [ sum([ matrix_A[i][j]*matrix_B[j][k] for j in range(m) ]) for k in range(l) ] for i in range(n) ]
    result=""

    for vector in matrix_C:
        for item in vector:
            result+=str(item)+" "
        result=result.rstrip()
        result+="\n"
    print(result.rstrip())

def inputError():
    '''
    print("input Error")
    return -1
    '''
 
    print("input Error")
    return -1
     
func()