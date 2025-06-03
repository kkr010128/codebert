a=[0]*26
w='abcdefghijklmnopqrstuvwxyz'
try:
    while True:
        s=list(input().upper())
        for i in s:
            if i=='A':
                a[0]+=1
            elif i=='B':
                a[1]+=1
            elif i=='C':
                a[2]+=1
            elif i=='D':
                a[3]+=1
            elif i=='E':
                a[4]+=1
            elif i=='F':
                a[5]+=1
            elif i=='G':
                a[6]+=1
            elif i=='H':
                a[7]+=1
            elif i=='I':
                a[8]+=1
            elif i=='J':
                a[9]+=1
            elif i=='K':
                a[10]+=1
            elif i=='L':
                a[11]+=1
            elif i=='M':
                a[12]+=1
            elif i=='N':
                a[13]+=1
            elif i=='O':
                a[14]+=1
            elif i=='P':
                a[15]+=1
            elif i=='Q':
                a[16]+=1
            elif i=='R':
                a[17]+=1
            elif i=='S':
                a[18]+=1
            elif i=='T':
                a[19]+=1
            elif i=='U':
                a[20]+=1
            elif i=='V':
                a[21]+=1
            elif i=='W':
                a[22]+=1
            elif i=='X':
                a[23]+=1
            elif i=='Y':
                a[24]+=1
            elif i=='Z':
                a[25]+=1 

except EOFError:
    pass

for i in range(26):
    print(w[i:i+1], ':', str(a[i]))