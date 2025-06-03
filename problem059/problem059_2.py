# coding: utf-8
# Here your code !
 
import math
 
def func():
    try:
        (rows,columns) = [ int(item) for item in input().rstrip().split(" ") ]
        data = [ [ int(item) for item in input().rstrip().split(" ") ] for i in range(rows) ]
    except:
        return inputError()
        
    [item.append(sum(item)) for item in data]
    data.append( [sum( [ item[i] for item in data ] ) for i in range(columns+1) ])
    
    result=""
    for row in data:
        for item in row:
            result += str(item)+" "
        result=result.rstrip()
        result += "\n"
    print(result.rstrip())

def inputError():
    '''
    print("input Error")
    return -1
    '''
 
    print("input Error")
    return -1
     
func()