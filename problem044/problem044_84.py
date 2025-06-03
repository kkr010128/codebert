a,b,c = map(int, input().split())

m=0
while b >=a:
    if c % b == 0 :
        m = m + 1

    else:
        pass
    b = b-1
    
print(m)