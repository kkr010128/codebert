import math
N=int(input())
if (N/1.08).is_integer()==True:
    S=int(N/1.08)
else:
    S=math.ceil(N/1.08)
if (S*1.08)//1==N:
    print(S)
else:
    print(':(')