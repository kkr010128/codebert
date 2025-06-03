H,A = input().split()
H = int(H)
A = int(A)
if H <= A :
    print('1')
elif not H % A == 0 :
    print(str(H//A + 1))
else :
    print(str(H//A))
