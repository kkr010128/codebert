N, X, T = [int(i) for i in input().split()]
 
q, r = divmod(N, X)
 
output = 0
if r > 0:
    output = (q+1) * T
else :
    output = q * T
    
print(output)