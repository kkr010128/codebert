k = int(input())
lis = [1,2,3,4,5,6,7,8,9]

i = 0
while i<9:
    X = []
    for L in lis:
        if i == 0 or L >= 10**i:
            s = str(L)
            if s[-1] == "0":
                X.append(10*L)
                X.append(10*L+1)
            elif s[-1] == "9":
                X.append(10*L+8)
                X.append(10*L+9)
            else:
                X.append(10*L+int(s[-1])-1)
                X.append(10*L+int(s[-1]))
                X.append(10*L+int(s[-1])+1)
    for x in X:
        lis.append(x)
    i += 1
print(lis[k-1])