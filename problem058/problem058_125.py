while(1):
    comb = []
    count =0
    inp = raw_input().split(" ")
    if inp[0] == "0" and inp[1] == "0":
        break
    for i in range(1,int(inp[0])+1):
        for j in range(1,int(inp[0])+1):
            if i == j:
                break
            sum = i + j
            if sum > int(inp[1]):
                j = int(inp[0])
                break
            for k in range(1,int(inp[0])+1):
                if i == j or i == k or j == k:
                    break
                sum = i + j + k
                if sum > int(inp[1]):
                    k = int(inp[0])
                    break
                if sum == int(inp[1]):
                    if not ([i,j,k] in comb or [i,k,j] in comb or [j,k,i] in comb or [j,i,k] in comb or [k,i,j]  in comb or [k,j,i] in comb):
                        comb.append([i,j,k])
                        count += 1
    print count
