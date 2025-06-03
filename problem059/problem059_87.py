while True:
    try:
        r,c = map(int,raw_input().split())
        if r == c == 0:
            break
    except EOFError:
        break
    
    array = []
    for i in range(r):
        array.append(map(int,raw_input().split()))
    
    # column sum
    # add a new sum-row 
    c_sum_row = [0 for ii in range(c)]
    for k in range(c):
        for j in range(r):
            c_sum_row[k] += array[j][k]
    array.append(c_sum_row)
    
    # row sum
    # append sum item to end of each row
    for k in range(r+1):
        array[k].append(sum(array[k]))
    
    for k in range(r+1):
        print ' '.join(map(str,array[k]))