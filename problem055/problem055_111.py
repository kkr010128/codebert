
import sys

def check(x_list, f, r, v):
    x_list[f][r] += v

def peo(x_list):
    for i in range(3):
        for j in range(10):
            sys.stdout.write(" %d" %(x_list[i][j]))
        print ("")

A_bill = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
B_bill = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
C_bill = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
D_bill = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

n = input()
for i in range(n):
    x = raw_input()
    b, f, r, v = x.split()
    b = int(b)
    f = int(f)
    r = int(r)
    v = int(v)
    
    if b == 1:
        check(A_bill, f-1,r-1,v)
    elif b == 2:
        check(B_bill, f-1,r-1,v)
    elif b == 3:
        check(C_bill, f-1,r-1,v)
    elif b == 4:
        check(D_bill, f-1,r-1,v)

peo(A_bill)
print("####################")
peo(B_bill)
print("####################")
peo(C_bill)
print("####################")
peo(D_bill)