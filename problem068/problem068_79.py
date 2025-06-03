tes = input()
for mak in range(int(input())) :
    ins = input().split()
    ins[1], ins[2] = int(ins[1]), int(ins[2])
    if ins[0] == 'replace' :
        tes = tes[ : (ins[1])] + ins[3] + tes[(ins[2] + 1) :]
    elif ins[0] == 'reverse' :
        tem = tes[ins[1] : ins[2] + 1]
        tem = tem[::-1]
        tes = tes.replace(tes[ins[1] : ins[2] + 1], tem)
    elif ins[0] == 'print' :
        print(tes[ins[1] : ins[2] + 1])