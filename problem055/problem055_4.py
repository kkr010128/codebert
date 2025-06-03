table = [[[ 0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())

i = 0
while i < n:
    b,f,r,v = (int(x) for x in input().split())
    
    table[b-1][f-1][r-1] += v

    i += 1

for i,elem_i in enumerate(table):           # building
    for j,elem_j in enumerate(elem_i):      # floor
        for k, elem_k in enumerate(elem_j): # room
            print (" " + str(elem_k), end='')
        print ("")
    if i != 3:
        print ("####################")
