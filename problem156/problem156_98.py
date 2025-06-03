X = int(input())

ok = False
for a in range(200):
    for b in range(200):
        if a**5 - b**5 == X:
            ok = True
            A, B = a, b
            break
        
        if a**5 + b**5 == X:
            ok = True
            A, B = a, -b
            break
    
    if ok == True:
        break

print(A, end=' ')
print(B)