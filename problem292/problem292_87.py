n=int(input())
A=input().split()
def findProductSum(A,n): 
  
    product = 0
    for i in range (n): 
        for j in range ( i+1,n): 
            product = product + int(A[i])*int(A[j])
    return product
print(findProductSum(A,n))