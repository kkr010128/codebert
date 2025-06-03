in1 = input().split()
A = int(in1[0])
B = int(in1[1])
if A>=1 and B>=1 and A<=9 and B<=9:
    print (A*B)
else:
    print(-1)