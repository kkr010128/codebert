n=input()
num_list=[int(x) for x in raw_input().split(" ")]

for idx in range(1, len(num_list)):
    print " ".join([str(x) for x in num_list])
    key=num_list[idx]
    jdx = idx - 1
    
    while jdx >= 0 and num_list[jdx] > key:
        num_list[jdx+1] = num_list[jdx]
        jdx -= 1
    num_list[jdx+1] = key
print " ".join([str(x) for x in num_list])