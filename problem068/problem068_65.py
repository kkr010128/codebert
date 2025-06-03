line = input()
n = int(input())
array = [[i for i in input().split()] for i in range(n)]
for i in range(n):
    if array[i][0] == "print":
        print(line[int(array[i][1]):int(array[i][2])+1])
    elif array[i][0] == "reverse":
        if array[i][1] !="0":
            reline = line[int(array[i][2]):int(array[i][1])-1:-1]
        else:
            reline = line[int(array[i][2])::-1]
        revara = list(line)
        for i2 in range(len(reline)):
            revara[int(array[i][1])+i2] = reline[i2]
        for i2 in range(len(revara)):
            if i2 ==0:
                line = revara[i2]
            else:
                line += revara[i2]
        
    elif array[i][0] == "replace":
        repara = list(line)
        inpara = list(array[i][3])
        for i2 in range(len(inpara)):
            repara[int(array[i][1])+i2] = inpara[i2]
        for i2 in range(len(repara)):
            if i2 ==0:
                line = repara[i2]
            else:
                line += repara[i2]