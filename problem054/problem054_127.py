table = [[ 0 for i in range(13)] for j in range(4)]

n = int(input())

i = 0 
while i < n:
    s,num = input().split()
    num = int(num)
    
    if   s == "S":
        table[0][num-1] = 1
    elif s == "H":
        table[1][num-1] = 1
    elif s == "C":
        table[2][num-1] = 1
    else:    # D 
        table[3][num-1] = 1

    i += 1

for i,elem_i in enumerate(table):
    for j,elem_j in enumerate(elem_i):
        if elem_j ==1:
            continue

        if i == 0:
            s_str='S'
        elif i == 1:
            s_str='H'
        elif i == 2:
            s_str='C'
        else:
            s_str='D'
        print (s_str + " " + str(j+1))
