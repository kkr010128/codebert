a, b = map(int, input().rstrip().split(" "))

if a > b:
    A = a
    B = b
else:
    A = b
    B = a

GCD = 1
while True:
    A, B = B, A%B
    
    if B == 0:
        break
    
print (str(A))