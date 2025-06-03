A,B,C = map(int,input().split())
if(A==B and B==C):
    print('No')
    exit()
if(A==B or A==C or B==C):
    print('Yes')
    exit()
else:
    print('No')