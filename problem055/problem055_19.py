n = int(input())
a =[' 0',' 0',' 0',' 0',' 0',' 0',' 0',' 0',' 0',' 0']
A_1 = a.copy()
A_2 = a.copy()
A_3 = a.copy()
B_1 = a.copy()
B_2 = a.copy()
B_3 = a.copy()
C_1 = a.copy()
C_2 = a.copy()
C_3 = a.copy()
D_1 = a.copy()
D_2 = a.copy()
D_3 = a.copy()
ren1 = [A_1,A_2,A_3]
ren2 = [B_1,B_2,B_3]
ren3 = [C_1,C_2,C_3]
ren4 = [D_1,D_2,D_3]
for i in range(n):
    b = input()
    c = b.split(' ')
    ren = int(c[0])
    kai = int(c[1])
    banme = int(c[2])
    nin = int(c[3])
    if nin < 0:
        if ren == 1:
            ren1[kai-1][banme-1] = ' %s'%(int(ren1[kai-1][banme-1])+nin)
        elif ren == 2:
            ren2[kai-1][banme-1] = ' %s'%(int(ren2[kai-1][banme-1])+nin)
        elif ren == 3:
            ren3[kai-1][banme-1] = ' %s'%(int(ren3[kai-1][banme-1])+nin)
        elif ren == 4:
            ren4[kai-1][banme-1] = ' %s'%(int(ren4[kai-1][banme-1])+nin)
    elif ren == 1:
        ren1[kai-1][banme-1] = ' %s'%(int(ren1[kai-1][banme-1])+nin)
    elif ren == 2:
        ren2[kai-1][banme-1] = ' %s'%(int(ren2[kai-1][banme-1])+nin)
    elif ren == 3:
        ren3[kai-1][banme-1] = ' %s'%(int(ren3[kai-1][banme-1])+nin)
    elif ren == 4:
        ren4[kai-1][banme-1] = ' %s'%(int(ren4[kai-1][banme-1])+nin)
print(''.join(A_1))
print(''.join(A_2))
print(''.join(A_3))
print('####################')
print(''.join(B_1))
print(''.join(B_2))
print(''.join(B_3))
print('####################')
print(''.join(C_1))
print(''.join(C_2))
print(''.join(C_3))
print('####################')
print(''.join(D_1))
print(''.join(D_2))
print(''.join(D_3))