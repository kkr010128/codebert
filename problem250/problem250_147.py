def prime(p):
    flag = True
    for i in range(2,(int(p**0.5)+1)):
        if p%i==0:
            flag = False
            break
    return flag

X = int(input())

while True:
    result = prime(X)
    if result:
        break
    else:
        X += 1

print(X)